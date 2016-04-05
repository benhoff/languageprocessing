import argparse
import pluginmanager
from languageprocessing.messaging import Messaging


def main(*args, **kwargs):
    """
    kwargs:
        text_address
        result_address
        context
    """
    plugin_manager = pluginmanager.PluginInterface()
    plugin_manager.set_entry_points('languageprocessing.analyzers')
    analyzers = plugin_manager.collect_entry_point_plugins()
    invoked_analyzers = [a() for a in analyzers]

    messager = Messaging(kwargs['text_address'],
                         kwargs['result_address'],
                         context=None,
                         analyzers=invoked_analyzers)

    messager.run()


def _get_kwargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text_address')
    parser.add_argument('--result_address')
    return vars(parser.parse_args())


if __name__ == '__main__':
    kwargs = _get_kwargs()
    main(**kwargs)
