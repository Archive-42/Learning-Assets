import { createWaitablePromise, encode, WaitablePromise } from '@algolia/client-common';
import { MethodEnum } from '@algolia/requester-common';
import { RequestOptions } from '@algolia/transporter';

import { DeleteByFiltersOptions, DeleteResponse, SearchIndex } from '../..';
import { waitTask } from '..';

export const deleteBy = (base: SearchIndex) => {
  return (
    filters: DeleteByFiltersOptions,
    requestOptions?: RequestOptions
  ): Readonly<WaitablePromise<DeleteResponse>> => {
    return createWaitablePromise<DeleteResponse>(
      base.transporter.write(
        {
          method: MethodEnum.Post,
          path: encode('1/indexes/%s/deleteByQuery', base.indexName),
          data: filters,
        },
        requestOptions
      ),
      (response, waitRequestOptions) => waitTask(base)(response.taskID, waitRequestOptions)
    );
  };
};
