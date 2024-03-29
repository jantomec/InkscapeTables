import sys
import inkex

class TablesExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--columns", type=int, help="Number of columns")
        pars.add_argument("--rows", type=int, help="Number of rows")

    def effect(self):
        # Dimensions for the table SVG
        columns = self.options.columns
        rows = self.options.rows

        column_width = 12
        row_height = 9

        table = inkex.Group()

        for i in range(columns):
            column = inkex.Group()
            for j in range(rows):
                rect = inkex.Rectangle(
                    x=str(i*column_width),
                    y=str(j*row_height),
                    width=str(column_width),
                    height=str(row_height),
                    style="stroke:black;stroke-width:0.4;fill:white"
                )
                column.append(rect)
            table.append(column)
        self.svg.get_current_layer().append(table)

if __name__ == '__main__':
    TablesExtension().run()