class Node(object):
    def __init__(self, file_path):
        self.n_set_name, self.data_array = self.get_node_information_from_file(file_path)

    def read_file(self, file_path):
        fil1 = open(file_path, 'r')
        lines = fil1.readlines()
        start = "*NODE,NSET=nall"
        end = "**HWCOLOR COMP          1    17"
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
        start = "*NODE,NSET="
        n_set_name = ""
        node_mat = []
        if head_line.__contains__(start):
            n_set_name = head_line[len(start):]
        else:
            print False
        for line in data_array:
            sub_array = line.split(",")
            node_id = int(sub_array[0].strip())
            x = float(sub_array[1].strip())
            y = float(sub_array[2].strip())
            z = float(sub_array[3].strip())
            node_mat.append([node_id, x, y, z])
        return n_set_name, node_mat

    def shift(self, node_id, dx, dy, dz):
        node_ID = node_id
        for nodes in self.data_array:
            if node_ID == nodes[0]:
                nodes[1] += float(dx)
                nodes[2] += float(dy)
                nodes[3] += float(dz)
                break
    print 'shift process is done'


    def set_name(self, name):
        self.n_set_name = name
        print("set nset_name to :" + name)

    def write(self, file_path):
        write_input = self.write_information_to_file(self.n_set_name, self. data_array, file_path)
        print 'write process is done'

    def write_information_to_file(self, n_set_name, data_array, file_path):
        fil2 = open(file_path, 'w')
        start = "*NODE,NSET="
        fil2.write(start + n_set_name + '\n')
        for nodes in data_array:
            line = str(nodes[0]) + ','+str(nodes[1]) + ','+str(nodes[2]) + ','+str(nodes[3])+'\n'
            fil2.write(line)
        fil2.close()

if __name__ == '__main__':
    input_file_path = "./../data/Modal.inp"
    output_file_path = "./../data/Modal_change.inp"
    node_input = Node(input_file_path)
    nodes = range(1, len(node_input.data_array))
    for i in nodes:
        node_input.shift(i, 1, 0, 0)
    node_input.set_name("nallnew")
    node_input.write(output_file_path)

















