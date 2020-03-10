# �������� ���� � ������� ������� ������ ������ https://www.minfin.ru/opendata/7710168360-BanksID/
import xml.etree.ElementTree as ET

filename = "ICB_bank_guarantees.xml"
tree = ET.parse(filename)

root = tree.getroot()

# � ������ ������ "������" - root - � ��� ����� ��������� ��� ���:
# <BanksFk xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://budgetminfin.ru/banks/1">
# �.�. � ���� BanksFk � �������� ���������� �������� ��������� xmlns="http://budgetminfin.ru/banks/1"
# ����������: ���� �� ������ xmlns:xsd � xmlns:xsi - ��� �� ��� ���������, ��� ������ ��� ���������, ������� �� ��������� ��������

# ��� �������� � xml, ���� � ��� ���� ����������

# ������� 1: ������������ ��������� � ������� ����,
# ��� ���: ���� banks - ����� ns:banks, ���� bank - ����� ns:bank � �.�.
ns = {"ns": "http://budgetminfin.ru/banks/1"}
banks = root.findall("ns:banks/ns:bank", ns)
print(len(banks))


# ������� 2: ���������� �� �����������. �� ������ ���� ������� ������� �� �� ��������� ����� (�� ����� ��� �� ������), ���� ������������ �������, ������� ������ ��� ���������� �� ������
# ������������� ����� �������� �����: https://homework.nwsnet.de/releases/45be/
def remove_namespace(doc, namespace):
    """Remove namespace in the passed document in place."""
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]


# ������� ���������� ���������� �������� remove_namespace
remove_namespace(tree, "http://budgetminfin.ru/banks/1")
# �������� � xml, ��� ��������
banks = root.findall("banks/bank")
print(len(banks))
