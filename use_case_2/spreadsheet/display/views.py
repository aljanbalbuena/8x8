from urllib.error import HTTPError

import pandas as pd

from django.conf import settings
from django.views.generic import TemplateView


class DisplayView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super().get_context_data()
        context["table_html"] = self.get_table_html()

        return context

    def get_table_html(self) -> str:
        """
        Retrieve a sheet from Google Docs and convert it into a sortable html table.
        More on the sorting script here: https://github.com/tofsjonas/sortable
        """
        kwargs = self.request.resolver_match.kwargs
        url = (
            f"{settings.GOOGLE_URL}/{kwargs['doc_id']}/export?format="
            f"{settings.EXPORT_FORMAT}"
        )
        if (sheet_id := kwargs.get("sheet_id")) is not None:
            url += f"&gid={sheet_id}"

        try:
            df = pd.read_csv(url)
        except HTTPError as error:
            # Can further expand to use custom exceptions if needed
            raise Exception("Failed to fetch sheet data.") from error

        # pandas attaches class="dataframe" to table tag upon conversion to html.
        # Replace class name with our recognizable attribute "sortable" to work
        # with the sorting script available.
        table_html = df.to_html()
        sortable = table_html.replace('class="dataframe"', 'class="sortable"')

        return sortable
