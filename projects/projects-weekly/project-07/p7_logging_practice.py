import logging
logging.basicConfig(filename='p7_test.log', filemode='w', format='%(asctime)s\
 %(levelname)s:%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
x = 10
log.debug('like grains of sand in an hourglass.')
log.info('the value of x is {}'.format(x))
# log.warning('That\'s a dead parrot')
# log.error('Foom')
# log.critical('I didn\'t come here for an argument')
