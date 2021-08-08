
class CSVReader:
    _items = None
    _items_map = None
    _idx = 0

    def _csv_string_to_array(self, csv_string : str) -> list:
        pos = csv_string.rfind(',')
        if pos == -1:
            return

        key, value = csv_string[:pos], csv_string[pos+1:]
        if key[0] == '"' and key[-1] == '"':
            key = key[1:-1]
        return [key,value]

    def __init__(self, file_path : str):
        try:
            f = open(file_path, encoding='UTF-8')
            self._items = f.read().split('\n')
        except UnicodeDecodeError:
            f = open(file_path, encoding='EUC-KR')
            self._items = f.read().split('\n')

    
    def next(self) -> list:
        it = self._items[self._idx]
        self._idx+=1
        return self._csv_string_to_array(it)

    def _index(self):
        if self._items_map is not None:
            return
        self._items_map = {}
        for item in self._items:
            itemAsArray = self._csv_string_to_array(item)
            if itemAsArray is None:
                return

            if len(itemAsArray) != 2:
                raise Exception('csv string format error')
            
            if itemAsArray[0] in self._items_map:                
                value = self._items_map[itemAsArray[0]]
            else:
                value = list()
            value.append(itemAsArray[1])
            self._items_map[itemAsArray[0]] = value

    def find(self, key : str) -> list:
        self._index()
        if key in self._items_map:
            return self._items_map[key]
        else:
            return None
        

# test
if __name__ == '__main__':
    c = CSVReader('./sample/sample-dataset.csv')
    print(c.find('테스트1,2'))