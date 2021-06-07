import PropTypes from 'typedefs/proptypes';

const propTypes = {
  tags: PropTypes.arrayOf(PropTypes.string).isRequired,
};

/**
 * List of tags.
 * Used in most pages that render snippet information.
 */
const TagList = ({ tags }) => (
  <p className='card-subtitle txt-050 fs-xs'>{tags.join(', ')}</p>
);

TagList.propTypes = propTypes;

export default TagList;
