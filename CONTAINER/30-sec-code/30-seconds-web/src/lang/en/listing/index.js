import { Tag } from 'blocks/utilities/tag';
import settings from 'settings/global';
/* istanbul ignore next */
const literals = {
  orders: {
    popularity: 'Recommended',
    alphabetical: 'Alphabetical',
    expertise: 'Expertise',
    newest: 'Newest',
  },
  featuredCollections: 'Featured Collections',
  collections: 'Snippet Collections',
  newBlogs: 'Latest Articles',
  topSnippets: 'Top Snippets',
  snippetList: 'Snippet List',
  blog: 'Articles',
  tag: t => `${Tag.format(t)}`,
  shortCodelang: l => `${l}`,
  shortCodelangTag: (l, t) => `${l} ${Tag.format(t)}`,
  shortBlogTag: t => `${Tag.format(t)}`,
  codelang: l => `${l} Snippets`,
  codelangTag: (l, t) => `${l} ${Tag.format(t)} Snippets`,
  blogTag: t => `${Tag.format(t)} Articles`,
  snippetCount: c => `${c} snippets`,
  pageDescription: (t, p) => {
    switch (t) {
      case 'language':
        return `Browse ${p.snippetCount} ${p.listingLanguage} code snippets for all your development needs on ${settings.websiteName}.`;
      case 'tag':
        return p.listingLanguage
          ? `Browse ${p.snippetCount} ${p.listingLanguage} ${Tag.format(
              p.listingTag
            )} code snippets for all your development needs on ${
              settings.websiteName
            }.`
          : `Browse ${p.snippetCount} ${Tag.format(
              p.listingTag
            )} articles for all your development needs on ${
              settings.websiteName
            }.`;
      case 'blog':
        return `Browse ${p.snippetCount} code articles for all your development needs on ${settings.websiteName}.`;
      case 'main':
        return `Browse ${
          p.snippetCount
        } ${settings.websiteDescription.toLowerCase()} on ${
          settings.websiteName
        }.`;
      case 'collections':
        return `Browse ${p.collectionCount} snippet collections on ${settings.websiteName}.`;
      default:
        return `Find ${settings.websiteDescription.toLowerCase()} on ${
          settings.websiteName
        }.`;
    }
  },
};

export default literals;
