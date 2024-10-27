import { BrowserRouter, Route, Routes } from "react-router-dom"
import InteractiveMapPage from "./pages/InteractiveMapPage"

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<InteractiveMapPage />}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
