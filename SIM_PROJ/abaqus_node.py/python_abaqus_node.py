class Node(object):
    def __init__(self, file_path, start, end):
        self.start = start
        self.end = end
        self.n_set_name, self.data_array = self.get_node_information_from_file(file_path)

    def read_file(self, file_path):
        with open(file_path, 'r') as fil1:
            lines = fil1.readlines()
            node_switch = False
            head_line = ""
            data_array = []
            for line in lines:
                if line.__contains__(start):
                    node_switch = True
                    head_line = line
                    continue
                elif line.__contains__(end):
                    node_switch = False
                    break
                if node_switch:
                    data_array.append(line)
            return head_line, data_array

    def get_node_information_from_file(self, file_path):
        head_line, data_array = self.read_file(file_path)
        n_set_name = ""
        node_mat = dict()
        if head_line.__contains__(self.start):
            n_set_name = head_line[len(self.start):]
        else:
            print False
        for line in data_array:
            sub_array = line.split(",")
            node_id = int(sub_array[0])
            x = float(sub_array[1])
            y = float(sub_array[2])
            z = float(sub_array[3])
            node_mat[node_id] = [x, y, z]
        return n_set_name, node_mat

    def shift(self, node_id, dx, dy, dz):
        lst = self.data_array.get(node_id)
        lst[0] += dx
        lst[1] += dy
        lst[2] += dz

    def set_name(self, name):
        self.n_set_name = name
        print("set nset_name to :" + name)

    def write_information_to_file(self, file_path):
        with open(file_path, 'w') as fil2:
            fil2.write(self.start + self.n_set_name + '\n')
            for key, lst in self.data_array.items():
                line = str(key) + ',' + ','.join([str(x) for x in lst]) + '\n'
                fil2.write(line)

if __name__ == '__main__':
    input_file_path = "./../data/Modal.inp"
    output_file_path = "./../data/Modal_change.inp"
    start = "*NODE,NSET="
    end = "**HWCOLOR COMP          1    17"
    node_input = Node(input_file_path, start, end)
    nodes = range(1, len(node_input.data_array))
    for i in nodes:
        node_input.shift(i, 1, 0, 0)
    node_input.set_name("nallnew")
    node_input.write_information_to_file(output_file_path)

















