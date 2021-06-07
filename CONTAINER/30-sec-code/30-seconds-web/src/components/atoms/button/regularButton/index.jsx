import PropTypes from 'typedefs/proptypes';
import { combineClassNames } from 'utils';

const propTypes = {
  onClick: PropTypes.func,
  className: PropTypes.string,
  children: PropTypes.oneOfType([
    PropTypes.node,
    PropTypes.arrayOf(PropTypes.node),
  ]),
  rest: PropTypes.any,
};

/**
 * Generic button component.
 */
const Button = ({
  onClick,
  className = '',
  children,
  ...rest // Needs props to have accessible name if only icon etc.
}) => (
  <button
    className={combineClassNames`btn fs-md ${className}`}
    onClick={onClick}
    {...rest}
  >
    {children}
  </button>
);

Button.propTypes = propTypes;

export default Button;
