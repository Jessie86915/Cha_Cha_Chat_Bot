from transitions.extensions import GraphMachine


class TocMachine ( GraphMachine ) :
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def Is_Going_To_Biological_Statistics(self, update):
        text = update.message.text
        return text.lower() == 'Go to 生物統計'

    def Is_Going_To_Industrial_Statistics(self, update):
        text = update.message.text
        return text.lower() == 'Go to 工業統計'

    def Is_Going_To_Commercial_Statistics(self, update):
        text = update.message.text
        return text.lower() == 'Go to 商業統計'

    def Is_Going_To_Mathematical_Statistics(self, update):
        text = update.message.text
        return text.lower() == 'Go to 數理統計'

    def On_Entering_Biological_Statistics(self, update):
        update.message.reply_text("I'm entering 生物統計")
        self.go_back(update)

    def On_Exiting_Biological_Statistics(self, update):
        print('Leaving 生物統計')

    def On_Entering_Industrial_Statistics(self, update):
        update.message.reply_text("I'm entering 工業統計")
        self.go_back(update)

    def On_Exiting_Industrial_Statistics(self, update):
        print('Leaving 工業統計')

    def On_Entering_Commercial_Statistics(self, update):
        update.message.reply_text("I'm entering 商業統計")
        self.go_back(update)

    def On_Exiting_Commercial_Statistics(self, update):
        print('Leaving 商業統計')

    def On_Entering_Mathematical_Statistics(self, update):
        update.message.reply_text("I'm entering 數理統計")
        self.go_back(update)

    def On_Exiting_Mathematical_Statistics(self, update):
        print('Leaving 數理統計')

    def Is_Going_To_Biological_Statistics_Teachers(self, update):
        text = update.message.text
        return text.lower() == 'Go to 生物統計老師'

    def On_Entering_Biological_Statistics_Teachers(self, update):
        update.message.reply_text("I'm entering 生物統計老師")
        self.go_back(update)

    def On_Exiting_Biological_Statistics_Teachers(self, update):
        print('Leaving 生物統計老師')

    def Is_Going_To_Industrial_Statistics_Teachers(self, update):
        text = update.message.text
        return text.lower() == 'Go to 工業統計老師'

    def On_Entering_Industrial_Statistics_Teachers(self, update):
        update.message.reply_text("I'm entering 工業統計老師")
        self.go_back(update)

    def On_Exiting_Industrial_Statistics_Teachers(self, update):
        print('Leaving 工業統計老師')

    def Is_Going_To_Commercial_Statistics_Teachers(self, update):
        text = update.message.text
        return text.lower() == 'Go to 商業統計老師'

    def On_Entering_Commercial_Statistics_Teachers(self, update):
        update.message.reply_text("I'm entering 商業統計老師")
        self.go_back(update)

    def On_Exiting_Commercial_Statistics_Teachers(self, update):
        print('Leaving 商業統計老師')

    def Is_Going_To_Mathematical_Statistics_Teachers(self, update):
        text = update.message.text
        return text.lower() == 'Go to 數理統計老師'

    def On_Entering_Mathematical_Statistics_Teachers(self, update):
        update.message.reply_text("I'm entering 數理統計老師")
        self.go_back(update)

    def On_Exiting_Mathematical_Statistics_Teachers(self, update):
        print('Leaving 數理統計老師')
