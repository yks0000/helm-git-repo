import yaml
import tabulate


def read_index_yaml(file_name: str = "index.yaml") -> dict:
    with open(file_name, 'r') as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return data['entries']


def generate_table(data, header):
    html = tabulate.tabulate(header, data, tablefmt="html", colalign=("center",))
    return html


def print_html(html: str, file_name: str = "helm.html", mode="w"):
    with open(file_name, mode) as html_file:
        html_file.write(html)


def parse_data():
    package_info = []
    index_data = read_index_yaml()
    total_packages = len(index_data)
    total_package_heading = ['Total Packages (Including All Version)']
    print_html(generate_table(total_package_heading, [[total_packages]]))

    package_info_heading = ['Name', 'Description', 'AppVersion', 'Chart Version', 'Created']

    for package_name, version_info in index_data.items():
        sorted(version_info, key=lambda row: (row['version'], row['created']), reverse=True)
        package = version_info[0]
        package_info.append([package['name'], package['description'],
                             package['appVersion'], package['version'],
                             package['created']])
    print_html(generate_table(package_info_heading, package_info), mode='a')


def main():
    parse_data()


if __name__ == '__main__':
    main()