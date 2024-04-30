
import os
import pyblish.api


class CollectCurrentWorkingDirectory(pyblish.api.ContextPlugin):
    """Inject the current working directory into Context"""

    order = pyblish.api.CollectorOrder
    label = "Current working directory"

    def process(self, context: pyblish.api.Context):
        context.data['cwd'] = os.getcwd()
