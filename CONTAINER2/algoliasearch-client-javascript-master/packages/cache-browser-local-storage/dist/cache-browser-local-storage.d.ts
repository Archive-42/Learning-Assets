import { Cache } from '@algolia/cache-common';

export declare type BrowserLocalStorageOptions = {
    /**
     * The cache key.
     */
    readonly key: string;
    /**
     * The native local storage implementation.
     */
    readonly localStorage?: Storage;
};

export declare function createBrowserLocalStorageCache(options: BrowserLocalStorageOptions): Cache;

export { }
