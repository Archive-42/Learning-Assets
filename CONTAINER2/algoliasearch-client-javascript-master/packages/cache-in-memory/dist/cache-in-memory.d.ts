import { Cache } from '@algolia/cache-common';

export declare function createInMemoryCache(options?: InMemoryCacheOptions): Cache;

export declare type InMemoryCacheOptions = {
    /**
     * If keys and values should be serialized using `JSON.stringify`.
     */
    readonly serializable?: boolean;
};

export { }
