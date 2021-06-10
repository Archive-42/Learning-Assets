export const useInput = initialValue => {
	const [value, setValue] = useState(initialValue);
	const handleChanges = updatedValue => {
		setValue(updatedValue);
	};
	return [value, setValue, handleChanges];
};

export default useInput;
