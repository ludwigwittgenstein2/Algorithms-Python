import random
import cProfile

def get_data():
        """Return 3 random integers between 0 and 0"""
        return random.sample(range(10),3)

def consume():
        """Displays a running average across list of integers sent to it."""
        running_sum = 0
        data_items_seen = 0

        while True:
                data = yield
                print "This is what data has Rick:",data
                data_items_seen += len(data)
                running_sum += sum(data)
                print ('Running average is {}'.format(running_sum/float(data_items_seen)))
def produce(consumer):
        """Produces a set of values and forwards them to pre-defined consumer function."""
        while True:
                data = get_data()
                print ('Produced {}'.format(data))
                consumer.send(data)
                yield

def main():
        consumer = consume()
        consumer.send(None)
        producer = produce(consumer)
        for _ in range(10):
                print('Producing...')
                next(producer)



if __name__ == '__main__':
        cProfile.run('print get_data)')
        main()
