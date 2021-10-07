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
    stats_data : dict
        dictionary with the statistics data
    """

    input_data = []
    stats_data = {}

    def build_stats(self):
        self.input_data = sorted(self.input_data)

        for value in self.input_data:
            self.stats_data[value] = {
                'start_position': self.input_data.index(value),
                'end_position': self.input_data.index(value)
            } if not self.stats_data.get(value) \
                else {
                'start_position': self.__get_start_position(value),
                'end_position': self.__get_end_position(value) + 1,
            }

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

    def __get_stats_data_by_index(self, index):
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

        if not self.stats_data.get(index):
            raise ValueError('Unable to find index %d' % index)

        return self.stats_data.get(index)

    def __get_start_position(self, index):
        """Private helper method to return the position of the first occurrence from a given element.

        Parameters
        ----------
        index : int
            Number/index to retrieve

        Raises
        ------
        ValueError
            If index/number does not exist.
        """

        return self.__get_stats_data_by_index(index).get('start_position')

    def __get_end_position(self, index):
        """Private helper method to return the position of the last occurrence found from a given element.

        Parameters
        ----------
        index : int
            Number/index to retrieve

        Raises
        ------
        ValueError
            If index/number does not exist.
        """

        return self.__get_stats_data_by_index(index).get('end_position')


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

        return len(self.input_data[start_position:end_position + 1])

    def greater(self, number):
        """Return quantity of elements with value greater than 'number' in constant time O(1)

        Parameters
        ----------
        number : int
            Element index
        """

        return len(self.input_data[self.__get_end_position(number)+1:len(self.input_data)])
