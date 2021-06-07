import fs from 'fs-extra';
import path from 'path';
import webfontsGenerator from 'webfonts-generator';
import { ArgsError } from 'blocks/utilities/error';
import { Logger } from 'blocks/utilities/logger';

/**
 * Serializes icons.
 */
export class IconSerializer {
  /**
   * Generates the icon font and CSS stylesheet from the provided icon files.
   * @param {Array<string>} fileList - An array of SVG file names.
   * @param {Array<object>} icons - An array of icon objects.
   * @param {object} options - An options object, containing the following:
   *  - `fontName`: Name of font and base name of font files.
   *  - `types`: Font file types to generate.
   *  - `outPath`: Directory for generated font files.
   *  - `cssPath`: Path for generated CSS file.
   *  - `fontRelativePath`: Relative font path for generated CSS file.
   *  - `cssSelector`: CSS selector for icons.
   *  - `cssClassName`: CSS class name for icons.
   *  - `cssClassPrefix`: CSS selector for icons.
   *  - `cssLanguageSelectors`: CSS language selectors.
   *
   * All `options` values default to values from `global.settings`.
   * @throws Will throw an error if `fileList` or `configs` is not supplied or empty.
   * @returns {Promise} A promise that will resolve when the icon font and CSS files
   *  have been written to disk.
   */
  static serialize = (
    fileList,
    icons,
    {
      fontName = global.settings.icons.fontName,
      types = global.settings.icons.types,
      outPath = global.settings.paths.rawAssetPath,
      cssPath = global.settings.paths.iconFontPath,
      fontRelativePath = global.settings.icons.fontRelativePath,
      cssTemplatePath = global.settings.icons.cssTemplatePath,
      cssSelector = global.settings.icons.cssSelector,
      cssClassName = global.settings.icons.cssClassName,
      cssClassPrefix = global.settings.icons.cssClassPrefix,
      cssLanguageSelectors = global.settings.icons.cssLanguageSelectors,
      cssLanguageChipSelector = global.settings.icons.cssLanguageChipSelector,
    } = {}
  ) => {
    if (!fileList || !fileList.length || !icons || !icons.length) {
      throw new ArgsError(
        "Missing required arguments. 'fileList' and 'configs' must be supplied and non-empty."
      );
    }

    const boundLog = Logger.bind('serializers.icon.serialize');
    boundLog(
      `Generating icon font and styles from ${fileList.length} files...`,
      'info'
    );

    const config = {
      files: fileList,
      dest: outPath,
      fontName,
      types,
      html: false,
      css: true,
      cssDest: cssPath,
      cssFontsUrl: fontRelativePath,
      cssTemplate: cssTemplatePath,
      templateOptions: {
        baseSelector: cssSelector,
        baseClassNames: cssClassName,
        classPrefix: cssClassPrefix,
        langSelectors: cssLanguageSelectors,
        chipSelector: cssLanguageChipSelector,
        langIcons: icons,
      },
    };

    return new Promise((resolve, reject) => {
      webfontsGenerator(config, (error, result) => {
        if (error) reject(error);
        else {
          const fileName = `${config.dest}/${config.fontName}`;
          boundLog(
            `Writing font to ${path.resolve(`${fileName}.${types[0]}`)}...`,
            'info'
          );
          ['svg', 'ttf', 'woff'].forEach(suffix =>
            fs.removeSync(`${fileName}.${suffix}`)
          );
          boundLog('Generating icon font and styles complete', 'success');
          resolve(result);
        }
      });
    });
  };
}
