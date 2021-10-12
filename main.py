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
    offset_mapping = []
    ordered_list = []
    counts = []

    def build_stats(self):
        # create list from max number
        self.counts = [0] * (max(self.input_data) + 1)
        self.offset_mapping = [0] * (max(self.input_data) + 1)

        # count total for each number
        for value in self.input_data:
            self.counts[value] += 1

        # recreate ordered array
        for index in range(len(self.counts)):
            if self.counts[index] > 0:
                for n in range(self.counts[index]):  # only if greater than 1 (more than one occurrence)
                    self.ordered_list.append(index)
                self.offset_mapping[index] = len(self.ordered_list)  # register last occurrence in list from this number


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

        if index >= len(self.offset_mapping):
            raise ValueError('Unable to find index %d' % index)

        return self.offset_mapping[index]

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

        return offset-self.counts[number]


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

        return self.__get_offset_by_index(number)

    def less(self, number):
        """Return quantity of elements with value smaller than 'number' in constant time O(1)

        Parameters
        ----------
        number : int
            Element index
        """

        return len(self.ordered_list[:self.__get_start_position(number)])


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

        return len(self.ordered_list[start_position:end_position])

    def greater(self, number):
        """Return quantity of elements with value greater than 'number' in constant time O(1)

        Parameters
        ----------
        number : int
            Element index
        """

        return len(self.ordered_list[self.__get_end_position(number):])



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
