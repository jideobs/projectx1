import json
from dataclasses import dataclass
from typing import List


@dataclass
class PageQueryingAttributes:
    query_param_name: str
    start_page: int
    end_page: int


@dataclass
class DataField:
    name: str
    class_name: str
    element_name: str


@dataclass
class DataHtmlAttributes:
    element_name: str
    row_html_attr: str
    fields: List[DataField]


@dataclass
class WebsiteMetadata:
    url: str
    page_query_attr: PageQueryingAttributes
    data_html_attr: DataHtmlAttributes

    @classmethod
    def from_json(cls, json_str: str):
        json_dict = json.loads(json_str)

        data_fields = []
        for data_field_dict in json_dict['data_html_attr']['fields']:
            data_fields.append(DataField(**data_field_dict))
        data_html_attr = DataHtmlAttributes(
            element_name=json_dict['data_html_attr']['element_name'],
            row_html_attr=json_dict['data_html_attr']['row_html_attr'],
            fields=data_fields
        )
        page_query_attr = PageQueryingAttributes(**json_dict['page_query_attr'])
        return cls(
            url=json_dict['url'],
            page_query_attr=page_query_attr,
            data_html_attr=data_html_attr)
