def before_scenario(context, scenario):
    context.web_driver = None


def after_scenario(context, scenario):
    if context.web_driver:
        try:
            context.web_driver.close()
        except Exception as e:
            print('Could not close web driver gracefully: {}'.format(e))
    context.web_driver = None
