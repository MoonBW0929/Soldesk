import { Navigate } from "react-router-dom";

const MoonP6 = () => {
    if (Math.random() > 0.5) {
        return <Navigate to="/p7.go" replace></Navigate>;
    }

    return <div>MoonP6</div>;
};

export default MoonP6;
