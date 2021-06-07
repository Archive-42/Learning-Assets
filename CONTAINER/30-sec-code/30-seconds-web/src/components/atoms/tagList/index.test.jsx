import { render, cleanup } from '@testing-library/react';
import TagList from './index';

describe('<TagList />', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = render(<TagList tags={['array', 'adapter', 'function']} />)
      .container;
  });

  afterEach(cleanup);

  it('should render correctly', () => {
    expect(wrapper.querySelectorAll('.card-subtitle')).toHaveLength(1);
  });

  it('should render a child for each passed tag name', () => {
    expect(wrapper.textContent).toBe('array, adapter, function');
  });
});
