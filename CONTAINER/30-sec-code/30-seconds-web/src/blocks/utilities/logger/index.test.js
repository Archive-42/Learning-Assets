import { magenta, blue, red, bold } from 'chalk';
import { Logger } from '.';
import { Writable } from 'stream';

describe('Logger', () => {
  const writeFn = jest.fn();
  const originalStream = Logger.outputStream;

  beforeAll(() => {
    Logger.outputStream = {
      write: writeFn,
    };
  });

  afterEach(() => {
    writeFn.mockClear();
  });

  describe('outputStream', () => {
    it('should be a Stream.Writable', () => {
      expect(originalStream instanceof Writable).toBe(true);
    });
  });

  describe('format', () => {
    it('should return the formatted message', () => {
      expect(Logger.format('Hello', 'magenta', 'bold')).toBe(
        bold(magenta('Hello'))
      );
    });

    it('should ignore unsupported formatters', () => {
      expect(Logger.format('Hello', 'magenta', 'foo')).toBe(magenta('Hello'));
    });
  });

  describe('log', () => {
    it('calls the write method of the outputStream', () => {
      Logger.log('Hello');
      expect(writeFn.mock.calls.length).toBe(1);
    });

    it('executes correctly with default options', () => {
      Logger.log('Hello');
      expect(writeFn.mock.calls[0][0]).toBe('Hello\n');
    });

    it('executes correctly for a given type as the sole argument', () => {
      Logger.log('Hello', 'info');
      expect(writeFn.mock.calls[0][0]).toBe(`${bold(blue('info'))}  Hello\n`);
    });

    it('executes correctly with an options object', () => {
      const opts = {
        breakLine: false,
        type: 'error',
        process: 'my-proc',
      };
      Logger.log('Hello', opts);
      expect(writeFn.mock.calls[0][0]).toBe(
        `${bold(red('errr'))}  [${bold(opts.process)}] Hello`
      );
    });

    it('falls back gracefully if passed incorrect options type', () => {
      Logger.log('Hello', 18);
      expect(writeFn.mock.calls[0][0]).toBe('Hello\n');
    });
  });

  describe('bind', () => {
    let boundLog;
    const procName = 'my-proc';

    beforeAll(() => {
      boundLog = Logger.bind(procName);
    });

    it('returns a bound instance of the logger function', () => {
      boundLog('Hello');
      expect(writeFn.mock.calls[0][0]).toBe(`[${bold(procName)}] Hello\n`);
    });
  });

  describe('breakLine', () => {
    it('logs an empty message of the appropriate type', () => {
      Logger.breakLine();
      expect(writeFn.mock.calls[0][0]).toBe(`${bold(blue('info'))}  \n`);
    });
  });

  describe('logProcessInfo', () => {
    it('logs the appropriate number of messages', () => {
      Logger.logProcessInfo();
      expect(writeFn.mock.calls.length).toBe(5);
    });
  });
});
