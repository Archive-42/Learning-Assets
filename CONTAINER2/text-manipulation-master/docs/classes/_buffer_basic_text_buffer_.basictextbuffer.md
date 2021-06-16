[text-manipulation](../README.md) > ["buffer/basic-text-buffer"](../modules/_buffer_basic_text_buffer_.md) > [BasicTextBuffer](../classes/_buffer_basic_text_buffer_.basictextbuffer.md)

# Class: BasicTextBuffer

## Hierarchy

**BasicTextBuffer**

## Implements

- [TextBuffer](../interfaces/_buffer_text_buffer_.textbuffer.md)

## Index

### Constructors

- [constructor](_buffer_basic_text_buffer_.basictextbuffer.md#constructor)

### Properties

- [lineDelimiter](_buffer_basic_text_buffer_.basictextbuffer.md#linedelimiter)
- [originalText](_buffer_basic_text_buffer_.basictextbuffer.md#originaltext)
- [table](_buffer_basic_text_buffer_.basictextbuffer.md#table)

### Methods

- [buildTable](_buffer_basic_text_buffer_.basictextbuffer.md#buildtable)
- [charAt](_buffer_basic_text_buffer_.basictextbuffer.md#charat)
- [columnExists](_buffer_basic_text_buffer_.basictextbuffer.md#columnexists)
- [getColumnCount](_buffer_basic_text_buffer_.basictextbuffer.md#getcolumncount)
- [getColumnRange](_buffer_basic_text_buffer_.basictextbuffer.md#getcolumnrange)
- [getLine](_buffer_basic_text_buffer_.basictextbuffer.md#getline)
- [getLineCount](_buffer_basic_text_buffer_.basictextbuffer.md#getlinecount)
- [getLineRange](_buffer_basic_text_buffer_.basictextbuffer.md#getlinerange)
- [getRangeText](_buffer_basic_text_buffer_.basictextbuffer.md#getrangetext)
- [getText](_buffer_basic_text_buffer_.basictextbuffer.md#gettext)
- [init](_buffer_basic_text_buffer_.basictextbuffer.md#init)
- [insertText](_buffer_basic_text_buffer_.basictextbuffer.md#inserttext)
- [insertTextAtLine](_buffer_basic_text_buffer_.basictextbuffer.md#inserttextatline)
- [isLineEmpty](_buffer_basic_text_buffer_.basictextbuffer.md#islineempty)
- [lineExists](_buffer_basic_text_buffer_.basictextbuffer.md#lineexists)
- [removeColumn](_buffer_basic_text_buffer_.basictextbuffer.md#removecolumn)
- [removeColumnRange](_buffer_basic_text_buffer_.basictextbuffer.md#removecolumnrange)
- [removeFirstLine](_buffer_basic_text_buffer_.basictextbuffer.md#removefirstline)
- [removeLastLine](_buffer_basic_text_buffer_.basictextbuffer.md#removelastline)
- [removeLine](_buffer_basic_text_buffer_.basictextbuffer.md#removeline)
- [removeLineRange](_buffer_basic_text_buffer_.basictextbuffer.md#removelinerange)
- [removeRange](_buffer_basic_text_buffer_.basictextbuffer.md#removerange)
- [replaceRange](_buffer_basic_text_buffer_.basictextbuffer.md#replacerange)
- [replaceTextInLine](_buffer_basic_text_buffer_.basictextbuffer.md#replacetextinline)

---

## Constructors

<a id="constructor"></a>

### constructor

⊕ **new BasicTextBuffer**(originalText: _`string`_, lineDelimiter?: _`string`_): [BasicTextBuffer](_buffer_basic_text_buffer_.basictextbuffer.md)

**Parameters:**

| Param                         | Type     | Default value |
| ----------------------------- | -------- | ------------- |
| originalText                  | `string` | -             |
| `Default value` lineDelimiter | `string` | &quot;&quot;  |

**Returns:** [BasicTextBuffer](_buffer_basic_text_buffer_.basictextbuffer.md)

---

## Properties

<a id="linedelimiter"></a>

### `<Private>` lineDelimiter

**● lineDelimiter**: _`string`_

---

<a id="originaltext"></a>

### `<Private>` originalText

**● originalText**: _`string`_

---

<a id="table"></a>

### `<Private>` table

**● table**: _`string`[][]_

---

## Methods

<a id="buildtable"></a>

### `<Private>` buildTable

▸ **buildTable**(text: _`string`_, lineDelimiter: _`string`_): `string`[][]

**Parameters:**

| Param         | Type     |
| ------------- | -------- |
| text          | `string` |
| lineDelimiter | `string` |

**Returns:** `string`[][]

---

<a id="charat"></a>

### charAt

▸ **charAt**(column: _`number`_, line: _`number`_): `string` &#124; `undefined`

**Parameters:**

| Param  | Type     |
| ------ | -------- |
| column | `number` |
| line   | `number` |

**Returns:** `string` &#124; `undefined`

---

<a id="columnexists"></a>

### columnExists

▸ **columnExists**(column: _`number`_, line: _`number`_): `boolean`

**Parameters:**

| Param  | Type     |
| ------ | -------- |
| column | `number` |
| line   | `number` |

**Returns:** `boolean`

---

<a id="getcolumncount"></a>

### getColumnCount

▸ **getColumnCount**(line: _`number`_): `number`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |

**Returns:** `number`

---

<a id="getcolumnrange"></a>

### getColumnRange

▸ **getColumnRange**(columnStart: _`number`_, columnEnd: _`number`_, line: _`number`_): `string`

**Parameters:**

| Param       | Type     |
| ----------- | -------- |
| columnStart | `number` |
| columnEnd   | `number` |
| line        | `number` |

**Returns:** `string`

---

<a id="getline"></a>

### getLine

▸ **getLine**(line: _`number`_): `string`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |

**Returns:** `string`

---

<a id="getlinecount"></a>

### getLineCount

▸ **getLineCount**(): `number`

**Returns:** `number`

---

<a id="getlinerange"></a>

### getLineRange

▸ **getLineRange**(lineStart: _`number`_, lineEnd: _`number`_): `string`

**Parameters:**

| Param     | Type     |
| --------- | -------- |
| lineStart | `number` |
| lineEnd   | `number` |

**Returns:** `string`

---

<a id="getrangetext"></a>

### getRangeText

▸ **getRangeText**(range: _[TextRange](../interfaces/_buffer_text_range_.textrange.md)_): `string`

**Parameters:**

| Param | Type                                                        |
| ----- | ----------------------------------------------------------- |
| range | [TextRange](../interfaces/_buffer_text_range_.textrange.md) |

**Returns:** `string`

---

<a id="gettext"></a>

### getText

▸ **getText**(): `string`

**Returns:** `string`

---

<a id="init"></a>

### `<Private>` init

▸ **init**(): `void`

**Returns:** `void`

---

<a id="inserttext"></a>

### insertText

▸ **insertText**(column: _`number`_, line: _`number`_, text: _`string`_): `void`

**Parameters:**

| Param  | Type     |
| ------ | -------- |
| column | `number` |
| line   | `number` |
| text   | `string` |

**Returns:** `void`

---

<a id="inserttextatline"></a>

### insertTextAtLine

▸ **insertTextAtLine**(line: _`number`_, text: _`string`_): `void`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |
| text  | `string` |

**Returns:** `void`

---

<a id="islineempty"></a>

### isLineEmpty

▸ **isLineEmpty**(line: _`number`_): `boolean`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |

**Returns:** `boolean`

---

<a id="lineexists"></a>

### lineExists

▸ **lineExists**(line: _`number`_): `boolean`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |

**Returns:** `boolean`

---

<a id="removecolumn"></a>

### removeColumn

▸ **removeColumn**(column: _`number`_, line: _`number`_): `void`

**Parameters:**

| Param  | Type     |
| ------ | -------- |
| column | `number` |
| line   | `number` |

**Returns:** `void`

---

<a id="removecolumnrange"></a>

### removeColumnRange

▸ **removeColumnRange**(columnStart: _`number`_, columnEnd: _`number`_, line: _`number`_): `void`

**Parameters:**

| Param       | Type     |
| ----------- | -------- |
| columnStart | `number` |
| columnEnd   | `number` |
| line        | `number` |

**Returns:** `void`

---

<a id="removefirstline"></a>

### removeFirstLine

▸ **removeFirstLine**(): `void`

**Returns:** `void`

---

<a id="removelastline"></a>

### removeLastLine

▸ **removeLastLine**(): `void`

**Returns:** `void`

---

<a id="removeline"></a>

### removeLine

▸ **removeLine**(line: _`number`_): `void`

**Parameters:**

| Param | Type     |
| ----- | -------- |
| line  | `number` |

**Returns:** `void`

---

<a id="removelinerange"></a>

### removeLineRange

▸ **removeLineRange**(lineStart: _`number`_, lineEnd: _`number`_): `void`

**Parameters:**

| Param     | Type     |
| --------- | -------- |
| lineStart | `number` |
| lineEnd   | `number` |

**Returns:** `void`

---

<a id="removerange"></a>

### removeRange

▸ **removeRange**(range: _[TextRange](../interfaces/_buffer_text_range_.textrange.md)_): [TextPosition](_buffer_text_position_.textposition.md)

**Parameters:**

| Param | Type                                                        |
| ----- | ----------------------------------------------------------- |
| range | [TextRange](../interfaces/_buffer_text_range_.textrange.md) |

**Returns:** [TextPosition](_buffer_text_position_.textposition.md)

---

<a id="replacerange"></a>

### replaceRange

▸ **replaceRange**(range: _[TextRange](../interfaces/_buffer_text_range_.textrange.md)_, text: _`string`_): [TextRange](../interfaces/_buffer_text_range_.textrange.md) &#124; `undefined`

**Parameters:**

| Param | Type                                                        |
| ----- | ----------------------------------------------------------- |
| range | [TextRange](../interfaces/_buffer_text_range_.textrange.md) |
| text  | `string`                                                    |

**Returns:** [TextRange](../interfaces/_buffer_text_range_.textrange.md) &#124; `undefined`

---

<a id="replacetextinline"></a>

### replaceTextInLine

▸ **replaceTextInLine**(line: _`number`_, lineText: _`string`_): `void`

**Parameters:**

| Param    | Type     |
| -------- | -------- |
| line     | `number` |
| lineText | `string` |

**Returns:** `void`

---
