import { useState, useEffect } from 'react'
import './styles/App.css'
import Navbar from './components/NavBar/Navbar.jsx'
import { Route, Routes } from 'react-router'
import Mainpage from './components/MainPage/Mainpage.jsx'
import PatchNotes from './components/PatchNotes/PatchNotes.jsx'


function App() {

  return (
    <>
      <Navbar />
      
      <Routes>
        <Route path='/' element={<Mainpage />} />
        <Route path='/patchnotes' element={<PatchNotes />} />
        <Route path='*' element={<h2>Whoops, nothing here!</h2>} />
      </Routes>
    </>
  )
}

export default App
