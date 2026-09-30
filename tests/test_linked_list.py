from linkedList import Node, SLL


def list_values(linked_list):
    values = []
    current = linked_list.head
    while current is not None:
        values.append(current.data)
        current = current.next
    return values


def test_node_defaults_to_empty():
    node = Node()

    assert node.data is None
    assert node.next is None


def test_node_stores_data_and_link():
    next_node = Node("Tue")
    node = Node("Mon")
    node.next = next_node

    assert node.data == "Mon"
    assert node.next is next_node


def test_sll_starts_empty():
    assert SLL().head is None


def test_at_start_prepends_node():
    linked_list = SLL()
    linked_list.AtStart("Tue")
    linked_list.AtStart("Mon")

    assert list_values(linked_list) == ["Mon", "Tue"]


def test_at_end_adds_to_empty_and_nonempty_lists():
    linked_list = SLL()
    linked_list.AtEnd("Mon")
    linked_list.AtEnd("Tue")

    assert list_values(linked_list) == ["Mon", "Tue"]


def test_inbetween_inserts_after_given_node():
    linked_list = SLL()
    linked_list.AtStart("Mon")
    middle_node = linked_list.head
    linked_list.AtEnd("Wed")

    linked_list.Inbetween(middle_node, "Tue")

    assert list_values(linked_list) == ["Mon", "Tue", "Wed"]


def test_inbetween_none_reports_failure_without_changing_list(capsys):
    linked_list = SLL()
    linked_list.AtStart("Mon")

    linked_list.Inbetween(None, "Tue")

    assert list_values(linked_list) == ["Mon"]
    assert "given node is not present" in capsys.readouterr().out


def test_delete_node_removes_head_middle_and_tail():
    linked_list = SLL()
    for value in ("Mon", "Tue", "Wed", "Thu"):
        linked_list.AtEnd(value)

    linked_list.DeleteNode("Mon")
    assert list_values(linked_list) == ["Tue", "Wed", "Thu"]

    linked_list.DeleteNode("Wed")
    assert list_values(linked_list) == ["Tue", "Thu"]

    linked_list.DeleteNode("Thu")
    assert list_values(linked_list) == ["Tue"]


def test_delete_missing_node_reports_failure_without_changing_list(capsys):
    linked_list = SLL()
    linked_list.AtStart("Mon")

    linked_list.DeleteNode("Tue")

    assert list_values(linked_list) == ["Mon"]
    assert "Node with data Tue not found" in capsys.readouterr().out


def test_delete_from_empty_list_reports_failure(capsys):
    linked_list = SLL()

    linked_list.DeleteNode("Mon")

    assert linked_list.head is None
    assert "Node with data Mon not found" in capsys.readouterr().out


def test_listprint_outputs_values_in_order(capsys):
    linked_list = SLL()
    linked_list.AtStart("Mon")
    linked_list.AtEnd("Tue")

    linked_list.listprint()

    assert capsys.readouterr().out.endswith("Mon\nTue\n")


def test_listprint_on_empty_list_outputs_nothing(capsys):
    SLL().listprint()

    assert capsys.readouterr().out == ""