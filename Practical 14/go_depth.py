"""
Practical 14: Working with Information

This script reads go_obo.xml and finds, for each Gene Ontology namespace,
the GO term with the greatest number of <is_a> elements.

It repeats the task using both DOM and SAX, then reports the time taken
by each API.

Speed comment for portfolio:
After running this script, check the final printed line and replace this
comment with the actual result, for example:
# SAX was fastest in my run.
"""

import os
import sys
import datetime
import xml.sax
from xml.dom import minidom, Node


TARGET_NAMESPACES = {
    "molecular_function": "molecular function",
    "biological_process": "biological process",
    "cellular_component": "cellular component",
}


def make_empty_results():
    """
    Create an empty results dictionary.

    Each namespace will store the best GO term found so far.
    """
    return {
        namespace: {
            "id": "",
            "name": "",
            "is_a_count": -1
        }
        for namespace in TARGET_NAMESPACES
    }


def normalise_namespace(namespace_text):
    """
    Convert namespace text into a consistent format.

    The XML usually uses values such as:
    molecular_function
    biological_process
    cellular_component
    """
    return namespace_text.strip().lower().replace(" ", "_")


def update_best_result(results, namespace, term_id, term_name, is_a_count):
    """
    Update the best result for a namespace if the current term has more
    <is_a> elements than the previous best term.
    """
    namespace = normalise_namespace(namespace)

    if namespace not in results:
        return

    if is_a_count > results[namespace]["is_a_count"]:
        results[namespace]["id"] = term_id.strip()
        results[namespace]["name"] = term_name.strip()
        results[namespace]["is_a_count"] = is_a_count


def get_first_tag_text(parent, tag_name):
    """
    Get the text inside the first child element with a given tag name.

    This joins all text nodes because XML text can sometimes be split
    into several pieces.
    """
    nodes = parent.getElementsByTagName(tag_name)

    if len(nodes) == 0:
        return ""

    text_parts = []

    for child in nodes[0].childNodes:
        if child.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
            text_parts.append(child.data)

    return "".join(text_parts).strip()


def analyse_with_dom(xml_file):
    """
    Analyse go_obo.xml using DOM.

    DOM reads the whole XML file into memory as a tree.
    """
    start_time = datetime.datetime.now()

    dom_tree = minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName("term")

    results = make_empty_results()

    for term in terms:
        term_id = get_first_tag_text(term, "id")
        term_name = get_first_tag_text(term, "name")
        namespace = get_first_tag_text(term, "namespace")

        is_a_elements = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_elements)

        update_best_result(
            results,
            namespace,
            term_id,
            term_name,
            is_a_count
        )

    end_time = datetime.datetime.now()
    time_taken = (end_time - start_time).total_seconds()

    return results, time_taken


class GOTermHandler(xml.sax.ContentHandler):
    """
    Custom SAX handler for reading GO terms.

    SAX reads the XML file as a stream and reacts to events:
    start of an element, end of an element, and character data.
    """

    def __init__(self):
        super().__init__()
        self.results = make_empty_results()

        self.in_term = False
        self.current_tag = ""

        self.term_id = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0

    def startElement(self, tag, attributes):
        """
        Called when SAX reaches an opening tag.
        """
        if tag == "term":
            self.in_term = True
            self.current_tag = ""

            self.term_id = ""
            self.term_name = ""
            self.namespace = ""
            self.is_a_count = 0

        elif self.in_term:
            self.current_tag = tag

            if tag == "is_a":
                self.is_a_count += 1

    def characters(self, content):
        """
        Called when SAX reads text inside an element.

        We use += because SAX can split text into multiple chunks.
        This follows the practical hint.
        """
        if not self.in_term:
            return

        if self.current_tag == "id":
            self.term_id += content
        elif self.current_tag == "name":
            self.term_name += content
        elif self.current_tag == "namespace":
            self.namespace += content

    def endElement(self, tag):
        """
        Called when SAX reaches a closing tag.
        """
        if tag == "term":
            update_best_result(
                self.results,
                self.namespace,
                self.term_id,
                self.term_name,
                self.is_a_count
            )

            self.in_term = False
            self.current_tag = ""

        elif self.in_term and tag == self.current_tag:
            self.current_tag = ""


def analyse_with_sax(xml_file):
    """
    Analyse go_obo.xml using SAX.

    SAX does not store the whole XML tree in memory.
    """
    start_time = datetime.datetime.now()

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = GOTermHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)

    end_time = datetime.datetime.now()
    time_taken = (end_time - start_time).total_seconds()

    return handler.results, time_taken


def print_results(title, results, time_taken):
    """
    Print the results in a readable format.
    """
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    for namespace, display_name in TARGET_NAMESPACES.items():
        result = results[namespace]

        print(f"\nNamespace: {display_name}")
        print(f"GO ID: {result['id']}")
        print(f"Name: {result['name']}")
        print(f"Number of <is_a> elements: {result['is_a_count']}")

    print(f"\nTime taken: {time_taken:.6f} seconds")


def main():
    """
    Main function.
    """
    if len(sys.argv) > 1:
        xml_file = sys.argv[1]
    else:
        xml_file = "go_obo.xml"

    if not os.path.exists(xml_file):
        print(f"Error: cannot find {xml_file}")
        print("Put go_obo.xml in the same folder as this script, or run:")
        print("python go_depth.py path/to/go_obo.xml")
        return

    print("Starting DOM analysis...")
    dom_results, dom_time = analyse_with_dom(xml_file)
    print("DOM analysis finished.")

    print("Starting SAX analysis...")
    sax_results, sax_time = analyse_with_sax(xml_file)
    print("SAX analysis finished.")

    print_results("DOM results", dom_results, dom_time)
    print_results("SAX results", sax_results, sax_time)

    print()
    print("=" * 60)
    print("Comparison")
    print("=" * 60)

    if dom_results == sax_results:
        print("DOM and SAX returned the same results.")
    else:
        print("Warning: DOM and SAX returned different results.")
        print("Check the parsing logic or the XML structure.")

    if dom_time < sax_time:
        print("Fastest API in this run: DOM")
    elif sax_time < dom_time:
        print("Fastest API in this run: SAX")
    else:
        print("DOM and SAX took the same time.")


if __name__ == "__main__":
    main()