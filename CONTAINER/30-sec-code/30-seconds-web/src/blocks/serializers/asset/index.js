import fs from 'fs-extra';
import path from 'path';
import sharp from 'sharp';
import glob from 'glob';
import { Logger } from 'blocks/utilities/logger';

// Image asset constants
const supportedExtensions = ['jpeg', 'jpg', 'png', 'webp', 'tif', 'tiff'];
const maxWidth = 800;
const outputQuality = 80;
// Icon asset constants
const dimensions = [48, 72, 96, 144, 192, 256, 384, 512];
const iconOutName = 'icon';

/**
 * Serializes assets.
 */
export class AssetSerializer {
  /**
   * Processes the given image asset, converting it to the correct size and quality.
   * @param {string} asset - The filename of the given asset.
   * @param {string} imageDirName - The output directory.
   * @returns {Promise} A promise that resolves when the file has finished writing to disk.
   */
  static processImageAsset = (asset, outDir) =>
    new Promise((resolve, reject) => {
      const fileName = asset.slice(asset.lastIndexOf('/'));
      const img = sharp(asset);
      return img.metadata().then(metadata => {
        const resizeWidth = Math.min(maxWidth, metadata.width);
        const name = fileName.slice(0, fileName.lastIndexOf('.'));
        const format = metadata.format;
        const resized = img.resize({ width: resizeWidth });
        return Promise.all([
          resized
            .toFormat(format, { quality: outputQuality })
            .toFile(`${outDir}/${fileName}`),
          resized
            .webp({ quality: outputQuality })
            .toFile(`${outDir}/${name}.webp`),
        ])
          .then(() => resolve())
          .catch(() => reject());
      });
    });

  /**
   * Prepares the assets directory.
   */
  static serialize = async () => {
    const boundLog = Logger.bind('serializers.asset.serialize');
    const {
      rawAssetPath: inPath,
      rawContentAssetPath: inContentPath,
      assetPath: outPath,
      rawContentPath: contentPath,
      staticAssetPath: staticAssetPath,
      publicPath,
    } = global.settings.paths;
    const configs = global.settings.configs;
    boundLog('Processing assets from config...', 'info');

    boundLog(
      `Copying static assets from ${path.resolve(inPath)} to ${path.resolve(
        outPath
      )}`,
      'info'
    );
    fs.ensureDirSync(outPath);
    await fs.copy(inPath, outPath);
    await fs.copy(inContentPath, outPath);
    boundLog('Static assets have been copied', 'success');

    boundLog(`Processing image assets from configuration files`, 'info');
    for (const cfg of configs) {
      const { images, dirName } = cfg;
      if (images && images.name && images.path) {
        fs.ensureDirSync(path.join(outPath, images.name));
        const assets = glob
          .sync(
            `${contentPath}/sources/${dirName}/${
              images.path
            }/*.@(${supportedExtensions.join('|')})`
          )
          .map(file => path.resolve(file));
        await Promise.all(
          assets.map(asset =>
            this.processImageAsset(asset, `${outPath}/${images.name}`)
          )
        );
      }
    }
    boundLog(
      `Processing image assets from configuration files complete`,
      'success'
    );

    boundLog('Processing icons...', 'info');
    await this.processIcons();
    boundLog(`Processing icons complete`, 'success');

    boundLog(
      `Copying assets from ${path.resolve(outPath)} to ${path.resolve(
        publicPath,
        staticAssetPath
      )}`,
      'info'
    );
    fs.ensureDirSync(path.join(publicPath, staticAssetPath));
    fs.copySync(outPath, path.join(publicPath, staticAssetPath));
    boundLog(`Copying assets complete`, 'success');

    return;
  };

  /**
   * Meant for manual use only via the console API.
   * Takes a PNG image and produces all the icon assets necessary for the website.
   */
  static processIcons = (iconName = '30s-icon.png') => {
    const { rawAssetPath: inPath, assetPath } = global.settings.paths;
    const iconPath = path.join(inPath, iconName);
    const outPath = path.join(assetPath, 'icons');

    fs.ensureDirSync(outPath);

    return new Promise((resolve, reject) => {
      const img = sharp(iconPath);
      return Promise.all([
        img.resize({ width: 32 }).png().toFile(`${outPath}/favicon-32x32.png`),
        ...dimensions.map(d =>
          img
            .resize({ width: d })
            .png()
            .toFile(`${outPath}/${iconOutName}-${d}x${d}.png`)
        ),
      ])
        .then(() => resolve())
        .catch(() => reject());
    });
  };
}
