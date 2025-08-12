import { useSelector } from "react-redux";
import NotLogin from "./sub_content/NotLogin";

const EatLogInquiry = () => {
    const subscriber = useSelector((store) => store.AccountSlice);

    if (!subscriber.login) return <NotLogin />;
    else {
        return <div>EatLogInquiry</div>;
    }
};

export default EatLogInquiry;
