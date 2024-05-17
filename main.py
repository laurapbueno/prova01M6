import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import typer
import sys

class TurtleDrawer(Node):
    # Classe para controlar e desenhar com a tartaruga no Turtlesim
  
    def __init__(self):
        # Inicializa o nó do ROS e cria um publicador para comandos de movimento da tartaruga

        super().__init__('turtle_drawer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move_turtle(self, linear, angular):
        # Move a tartaruga com base na velocidade linear e angular fornecidas

        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.publisher.publish(twist)

def main():
    rclpy.init()
    app = typer.Typer()
    turtle_drawer = TurtleDrawer()
    comandos = []

    @app.command(name="CLI")
    def CLI():
        while True:
            opcao = typer.prompt("Escolha uma opção: (Digite 'sair' para encerrar)")
            if opcao.lower() == "sair":
                executar(comandos, turtle_drawer)
                break
            else:
                comandos.append(opcao)

    def executar(comandos, turtle_drawer):
        for comando in comandos:
            if comando == "Sair do Programa":
                sys.exit()
            elif comando == "Adicionar Comando":
                x = float(typer.prompt("X: "))
                y = float(typer.prompt("Y: "))
                turtle_drawer.move_turtle(x, y)

    app()

if __name__ == "__main__":
    main()
