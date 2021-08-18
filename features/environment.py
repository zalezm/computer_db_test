def before_scenario(context, scenario):
    context.web_driver = None
    context.current_page = None

def before_step(context, step):
    print('------ Start Step ------')


def after_step(context, step):
    print('------ End Step ------')


def after_scenario(context, scenario):
    # cleanup current POM after each scenario to avoid lingering references to web drivers
    if context.current_page:
        context.current_page = None

    # cleanup web driver object after each scenario
    if context.web_driver:
        try:
            context.web_driver.close()
        except Exception as e:
            print('Could not close web driver gracefully: {}'.format(e))
    context.web_driver = None
