class DataCapture:
    """
    A class used to accepts numbers and returns an object for querying
    statistics about the inputs. Specifically, the returned object supports
    querying how many numbers in the collection are less than a value, greater
    than a value, or within a range.
    ...

    Attributes
    ----------
    input_data : list
        a list of integers provided by user
    offset_mapping : dict
        dictionary with the offset data
    """

    input_data = []
    offset_mapping = {}

    def build_stats(self):
        """
        Sort array using Radix Sort(*), building an offset mapping to find elements using n(1)
        * Radix sort logic reused from:  https://www.programiz.com/dsa/radix-sort
        """

        # Get maximum element
        max_element = max(self.input_data)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            size = len(self.input_data)
            output = [0] * size
            count = [0] * 10

            # Calculate count of elements
            for i in range(0, size):
                index = self.input_data[i] // place
                count[index % 10] += 1

            # Calculate cumulative count
            for i in range(1, 10):
                count[i] += count[i - 1]

            # Place the elements in sorted order
            i = size - 1
            while i >= 0:
                index = self.input_data[i] // place
                output[count[index % 10] - 1] = self.input_data[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, size):
                self.input_data[i] = output[i]
                if not self.offset_mapping.get(output[i]):
                    self.offset_mapping[output[i]] = {
                        'count': 1,
                        'offset': i
                    }
                else:
                    self.offset_mapping[output[i]] = {
                        'count': self.offset_mapping[output[i]].get('count') + 1,
                        'offset': i
                    }

            place *= 10

        return self.input_data

    def add(self, number):
        """Append a new element to input_data model attribute in constant time O(1)

        Parameters
        ----------
        number : int
            Positive integer number

        Raises
        ------
        ValueError
            If value provided is not blank or if it's not a positive integer
        """

        if not number or type(number) != int or number < 0:
            raise ValueError('%s is not a valid value. Please, provide a positive integer number.' % number)

        self.input_data.append(number)

    def __get_offset_by_index(self, index):
        """Private helper method to return an element from stats list from a given index.

        Parameters
        ----------
        index : int
            Number/index to retrieve

        Raises
        ------
        ValueError
            If index/number does not exist.
        """

        if not self.offset_mapping.get(index):

            raise ValueError('Unable to find index %d' % index)

        return self.offset_mapping.get(index)

    def __get_start_position(self, number):
        """Private helper method to return the position of the first occurrence from a given element.

        Parameters
        ----------
        number : int
            Number/index to retrieve

        Raises
        ------
        ValueError
            If index/number does not exist.
        """

        offset = self.__get_offset_by_index(number)

        return (offset.get('offset')+1) - offset.get('count')


    def __get_end_position(self, number):
        """Private helper method to return the position of the last occurrence found from a given element.

        Parameters
        ----------
        number : int
            Number/index to retrieve

        Raises
        ------
        ValueError
            If index/number does not exist.
        """

        # offset = self.offset_mapping[number]
        offset = self.__get_offset_by_index(number)

        return offset.get('offset') + 1

    def less(self, number):
        """Return quantity of elements with value smaller than 'number' in constant time O(1)

        Parameters
        ----------
        number : int
            Element index
        """

        return len(self.input_data[:self.__get_start_position(number)])


    def between(self, start_number, end_number):
        """Return quantity of elements with value between 'start_number' and 'end_number' (including themselves),
        in constant time O(1)

        Parameters
        ----------
        start_number : int
            Start number
        end_number : int
            Element index
        """

        start_position = self.__get_start_position(start_number)
        end_position = self.__get_end_position(end_number)

        return len(self.input_data[start_position:end_position])

    def greater(self, number):
        """Return quantity of elements with value greater than 'number' in constant time O(1)

        Parameters
        ----------
        number : int
            Element index
        """

        return len(self.input_data[self.__get_end_position(number):])



if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.build_stats()
    print(capture.less(4))  # should return 2 (only two values 3, 3 are less than 4)
    print(capture.between(3, 6))  # should return 4 (3, 3, 4 and 6 are between 3 and 6)
    print(capture.greater(4))  # should return 2 (6 and 9 are the only two values greater than 4)
