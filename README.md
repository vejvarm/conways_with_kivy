<h1>Conway's game of life utilizing <a href="https://kivy.org">Kivy</a> GUI framework</h1>

<h2> Running the app</h2>
<p>
  Run main.py with <a href="https://kivy.org">Kivy</a> and <a href="http://www.numpy.org/">NumPy</a> modules installed in your Python 3 interpreter.
</p>

<p>
  Window with a grid of cells and 4 buttons at the bottom should open. The cells can be clicked to change their state (alive/dead). This way you can manually influence the generation even when "Auto-Run" button is enabled.
<ul>
  <li>The <b>Random</b> button generates random cell states throughout the whole grid with certain bias toward dead cells.</li>
  <li>The <b>Clear</b> button resets all the cells to dead state.</li>
  <li>The <b>Next Gen</b> button calculates and shows the next generation of cell states on the grid.</li>
  <li>The <b>Auto-Run</b> button toggles automatic generation of new generation of cell states every 0.1 second</li>
</ul>
</p>

<p>
  If you want a smaller or bigger grid of cells, you can manually change the FIELD instance variables rows and cols of named tuple field in the main.py file. For higher (rows, cols) numbers the app is very memory consuming. I wouldn't recommend sizes over 100x100.
</p>

<p>
  Initial GUI design inspired by Amanda Hogan's <a href="https://www.youtube.com/watch?v=5on8Ybe41tE">A Basic Conways implementation in Kivy</a>.
  
  I also recommend this great <a href="https://youtu.be/B79miUFD_ss">Kivy Tutorial</a> by Derek Banas for anyone who is new to Kivy and would like to start learning it.
  
  For a demonstration video of the app, visit my <a href="https://www.youtube.com/watch?v=k9kcgdP8aLY">YouTube channel</a>.
</p>
