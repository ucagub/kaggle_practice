import { BrowserRouter, Route, Router, Routes } from "react-router-dom"
import HomePage from "./pages/HomePage"

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<HomePage />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
