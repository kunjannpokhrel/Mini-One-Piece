<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />

<div align="center">

  <h3 align="center">Mini One Piece</h3>

  <p align="center">
    A 2D One Piece-inspired platformer game built with Python and Pygame.
    <br /><br />
    <a href="https://github.com/kunjannpokhrel/Mini-One-Piece"><strong>Explore the project »</strong></a>
    <br /><br />
    <a href="https://github.com/kunjannpokhrel/Mini-One-Piece/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/kunjannpokhrel/Mini-One-Piece/issues">Request Feature</a>
  </p>

</div>


## About The Project

Mini One Piece is a 2D platformer game inspired by the One Piece universe, built from scratch using Python and Pygame.

The project follows Luffy through a simple combat encounter against Captain Alvida. The game includes a loading screen, game states, character movement, jumping, attacks, animations, sound effects, health bars, enemy animations, and a victory screen.

The main goal of the project is to learn pygame by building the systems myself instead of relying on a game engine and a step towards game development.

### Features

* 🎮 **2D Platformer** 
* ⚔️ **Combat System**
* 💥 **Attack Animations**
* 👊 **Sound Effects** 
* ❤️ **Health System** 
* 👾 **Enemy Animation** 
* 🗺️ **Game States**
* 🖼️ **Custom Artwork** 
* 🔄 **Restart System**
* ⛶ **Fullscreen Support**

## Built With

<p align="left">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://www.pygame.org/">
    <img src="https://img.shields.io/badge/Pygame-00A86B?style=for-the-badge&logo=python&logoColor=white" alt="Pygame">
  </a>
  <a href="https://github.com/">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/2D%20Game%20Development-000000?style=for-the-badge" alt="2D Game Development">
</p>

### Core Systems

| System                   | Description                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| **Game States**          | Controls loading, menu, level, and ending screens.                          |
| **Player Movement**      | Handles horizontal movement, jumping, gravity, and boundaries.              |
| **Combat**               | Includes multiple Luffy attacks with different damage ranges.               |
| **Animation**            | Uses sprite frames and timers to create character animations.               |
| **Health System**        | Tracks Luffy's HP and Captain Alvida's HP.                                  |
| **Audio System**         | Handles background music, attack sounds, jump sounds, and character sounds. |
| **Collision Boundaries** | Keeps the player inside the playable area and on the ground.                |

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure Python is installed on your computer.

You can check your Python installation with:

```sh
python --version
```

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/kunjannpokhrel/Mini-One-Piece.git
   ```

2. Enter the project directory:

   ```sh
   cd Mini-One-Piece
   ```

3. Install Pygame:

   ```sh
   pip install pygame
   ```

4. Run the game:

   ```sh
   python main.py
   ```

> **Note:** The game currently expects its asset files to remain in the project directory.

## Controls

| Key                      | Action                     |
| ------------------------ | -------------------------- |
| **A / Left Arrow**       | Move Left                  |
| **D / Right Arrow**      | Move Right                 |
| **W / Up Arrow / Space** | Jump                       |
| **J**                    | Luffy's Arm Stretch Attack |
| **K**                    | Gatling Attack             |
| **F11 / F**              | Toggle Fullscreen          |
| **Esc**                  | Exit Game                  |
| **Enter**                | Continue / Restart         |

## Gameplay

The current playable section features a boss battle against Captain Alvida.


### Boss Fight

Captain Alvida currently has **500 HP**.

Luffy has two available attacks:

| Attack             | Key | Damage |
| ------------------ | --- | ------ |
| **Arm Stretch**    | J   | 20 HP  |
| **Gatling Attack** | K   | 50 HP  |

The fight also includes attack animations, enemy animations, health display, sound effects, and a defeat animation.

## Repository Status

**In Development**<br>

This was created just to understand pygame but not sure if ill ever return to tthis project but one day I think I will.




## Contributing

This is mainly a personal learning project, but suggestions and improvements are welcome.

If you have a suggestion that would improve the project, feel free to fork the repository, make your changes, and open a pull request. You can also open an issue if you have an idea for a new feature or improvement.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top Contributors

<a href="https://github.com/kunjannpokhrel/Mini-One-Piece/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kunjannpokhrel/Mini-One-Piece" alt="top contributors" />
</a>


## License

This project is licensed under the **MIT License**.

Copyright (c) 2026 Kunjan Pokhrel

See the [LICENSE](LICENSE) file for the full license text.

## Contact

**Kunjan Pokhrel**

📧 email: [kunjannpokhrel@gmail.com](mailto:kunjannpokhrel@gmail.com)<br>
🔗 linkedIn: [www.linkedin.com/in/kunjanpokhrel](https://www.linkedin.com/in/kunjanpokhrel)<br>
💻 gitHub: [@kunjannpokhrel](https://github.com/kunjannpokhrel)

## Acknowledgments

* [Pygame](https://www.pygame.org/)
* [Python](https://www.python.org/)
* [GitHub](https://github.com/)
* One Piece — for the inspiration behind the game
* The creators of the artwork, sprites, music, and sound assets used in the project

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/kunjannpokhrel/Mini-One-Piece.svg?style=for-the-badge
[contributors-url]: https://github.com/kunjannpokhrel/Mini-One-Piece/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kunjannpokhrel/Mini-One-Piece.svg?style=for-the-badge
[forks-url]: https://github.com/kunjannpokhrel/Mini-One-Piece/network/members
[stars-shield]: https://img.shields.io/github/stars/kunjannpokhrel/Mini-One-Piece.svg?style=for-the-badge
[stars-url]: https://github.com/kunjannpokhrel/Mini-One-Piece/stargazers
[issues-shield]: https://img.shields.io/github/issues/kunjannpokhrel/Mini-One-Piece.svg?style=for-the-badge
[issues-url]: https://github.com/kunjannpokhrel/Mini-One-Piece/issues
[license-shield]: https://img.shields.io/github/license/kunjannpokhrel/Mini-One-Piece.svg?style=for-the-badge
[license-url]: https://github.com/kunjannpokhrel/Mini-One-Piece/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kunjanpokhrel