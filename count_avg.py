class Average:
    def count_average(self, arr: list[float]) -> float:
        return sum(arr) / len(arr)

    def compare_averages(self, arr1: list[float], arr2: list[float]) -> str:
        assert len(arr1) > 0, f'{arr1} should not be empty'
        assert len(arr2) > 0, f'{arr2} should not be empty'
        average_1 = self.count_average(arr1)
        average_2 = self.count_average(arr2)

        if average_1 == average_2:
            return 'Средние значения равны'

        if average_1 > average_2:
            return 'Первый список имеет большее среднее значение'

        return 'Второй список имеет большее среднее значение'