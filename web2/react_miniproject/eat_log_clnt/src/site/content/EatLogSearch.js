import { useSelector } from "react-redux";
import NotLogin from "./sub_content/NotLogin";

const EatLogSearch = () => {
    const subscriber = useSelector((store) => store.AccountSlice);

    if (!subscriber.login) return <NotLogin />;
    else {
        return <div>EatLogSearch</div>;
    }
};

export default EatLogSearch;
