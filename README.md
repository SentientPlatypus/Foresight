<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Sentientplatypus/Foresight">
    <img src="flaskApp\static\images\ForesightLogo.png" alt="Logo">
  </a>

<h3 align="center">Foresight</h3>

  <p align="center">
    LSTM stock forecast implemented in an accessible web format.
    <br /> 
    <a href="https://github.com/Sentientplatypus/Foresight"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://foresight.sentientplatypu.repl.co">View Website</a>
    .
    <a href="https://github.com/Sentientplatypus/Foresight-API">View API</a>
    ·
    <a href="https://github.com/Sentientplatypus/Foresight/issues">Report Bug</a>
    ·
    <a href="https://github.com/Sentientplatypus/Foresight/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="flaskApp\static\images\image.png" alt="Logo">

The Foresight is a webapp that does stock price prediction with TensorFlow's LSTM dense model.
Foresight splits its responsibilities into 2 applications: The webapp, and the Foresight API.
The webapp is responsible for displaying content, while the API does the HUGE amount of webscraping, and actually has the LSTM. I did this, because I needed to access data in javascript that is only available with python libraries. <br>
You may be wondering, why webscraping? Well thats because google finance has a LOT of helpful information!
<img src="flaskApp\static\images\gf.png" alt="Logo">

Unfortunately, 
<img src="flaskApp\static\images\discontinued.png" alt="Logo">
So I webscraped the information!
In hindsight, the webscraping does slow things down, A LOT. I learned from this mistake in my latest web implementation of a model at <a href="https://github.com/Beluga-Sturgeon">Beluga Sturgeon Financial</a></li> (this time its a reinforcement learning model).

But it is what it is! We learn.
Foresight took a lot of work. Routing, Styling, Scripting, Webscraping, Machine learning, integration and deployment were all things that needed to happen.
it was daunting at first, but my enthusiasm increased as things started coming together, especially after integrating the graph (Huge thanks to anychart)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python Badge][python]][python-url]
* [![heroku badge][heroku]][heroku-url]
* [![tf badge][tf]][tf-url]
* [![flask badge][flask]][flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

First clone this repository.  Then, you want pip freeze the requirements, or just use replit (i used replit for the application, and heroku for the API)

### Prerequisites

To get requirements, just 
* npm
  ```sh
  pip freeze > requirements.txt
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/Sentientplatypus/Foresight.git
   ```

And run `wsgi.py`. Its plug and play.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] Create the model
- [X] Create the website
- [X] Create the API 
- [X] Deploy

See the [open issues](https://github.com/Sentientplatypus/Foresight/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Geneustace Wicaksono - [My Website](https://genewica.herokuapp.com) - geneustacewicaksono@yahoo.com

Project Link: [https://github.com/Sentientplatypus/Foresight](https://github.com/Sentientplatypus/Foresight)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Sentientplatypus/Foresight.svg?style=for-the-badge
[contributors-url]: https://github.com/Sentientplatypus/Foresight/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Sentientplatypus/Foresight.svg?style=for-the-badge
[forks-url]: https://github.com/Sentientplatypus/Foresight/network/members
[stars-shield]: https://img.shields.io/github/stars/Sentientplatypus/Foresight.svg?style=for-the-badge
[stars-url]: https://github.com/Sentientplatypus/Foresight/stargazers
[issues-shield]: https://img.shields.io/github/issues/Sentientplatypus/Foresight.svg?style=for-the-badge
[issues-url]: https://github.com/Sentientplatypus/Foresight/issues
[license-shield]: https://img.shields.io/github/license/Sentientplatypus/Foresight.svg?style=for-the-badge
[license-url]: https://github.com/Sentientplatypus/Foresight/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: flaskApp\static\images\image.png
[jumper]: images/jumper.png
[body]: images/body.png
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.com
[heroku]: https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white
[heroku-url]: https://heroku.com
[tf]: 	https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[tf-url]: https://tensorflow.com
[flask]: 	https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.com
