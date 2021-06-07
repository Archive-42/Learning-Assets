import { MarkdownParser } from '.';

describe('MarkdownParser', () => {
  let snippetResult, blogResult;
  beforeAll(() => {
    snippetResult = MarkdownParser.parseSegments(
      {
        texts: {
          fullDescription: 'This is a `snippet` *description*.',
          description: 'This is...',
        },
        codeBlocks: {
          src: '```js\nHello\n```',
          example: '```js\nHi\n```',
        },
      },
      {
        isBlog: false,
        type: 'snippet',
        assetPath: '/assets',
        langData: [],
      }
    );
    blogResult = MarkdownParser.parseSegments(
      {
        texts: {
          fullDescription: 'This is a **blog**.\n\n* Hi\n* Hello\n',
          description: 'This is...',
        },
        codeBlocks: {},
      },
      {
        isBlog: true,
        type: 'list',
        assetPath: '/assets',
        langData: [],
      }
    );
  });

  describe('parseSegments', () => {
    it('returns the correct results for normal snippets', () => {
      expect(Object.keys(snippetResult).sort()).toEqual(
        ['description', 'example', 'fullDescription', 'src'].sort()
      );
    });

    it('returns the correct results for blog snippets', () => {
      expect(Object.keys(blogResult).sort()).toEqual(
        ['description', 'fullDescription'].sort()
      );
    });
  });
});
