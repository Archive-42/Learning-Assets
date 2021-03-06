import { Cache as Cache_2 } from '@algolia/cache-common';

export declare type Cache = {
    /**
     * Gets the value of the given `key`.
     */
    readonly get: <TValue>(key: object | string, defaultValue: () => Readonly<Promise<TValue>>, events?: CacheEvents<TValue>) => Readonly<Promise<TValue>>;
    /**
     * Sets the given value with the given `key`.
     */
    readonly set: <TValue>(key: object | string, value: TValue) => Readonly<Promise<TValue>>;
    /**
     * Deletes the given `key`.
     */
    readonly delete: (key: object | string) => Readonly<Promise<void>>;
    /**
     * Clears the cache.
     */
    readonly clear: () => Readonly<Promise<void>>;
};

export declare type CacheEvents<TValue> = {
    /**
     * The callback when the given `key` is missing from the cache.
     */
    readonly miss: (value: TValue) => Readonly<Promise<any>>;
};

export declare function createFallbackableCache(options: FallbackableCacheOptions): Cache;

export declare function createNullCache(): Cache;

export declare type FallbackableCacheOptions = {
    /**
     * List of caches order by priority.
     */
    readonly caches: readonly Cache_2[];
};

export { }
