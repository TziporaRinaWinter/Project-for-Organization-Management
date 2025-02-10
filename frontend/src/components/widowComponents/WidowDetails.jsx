import React, { useEffect, useState } from "react";
import WidowService from "../../services/WidowService";
import {
  Box,
  TextField,
  Button,
  Paper,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Typography,
  Grid2,
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const WidowDetails = ({ widowId }) => {
  const [widow, setWidow] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ age: 0 });
  const widowService = new WidowService();

  useEffect(() => {
    const loadWidow = async () => {
      try {
        const data = await widowService.getWidowById(widowId);
        setWidow(data[0]);
        setFormData(data[0]);
        // Calculate age
        const age = calculateAge(data[0].birth_date);
        setFormData((prev) => ({ ...prev, age }));
      } catch (err) {
        console.error(err.message);
      }
    };
    loadWidow();
  }, [widowId]);

  useEffect(() => {
    if (formData.birth_date) {
      const age = calculateAge(formData.birth_date);
      setFormData((prev) => ({ ...prev, age }));
    }
  }, [formData.birth_date]);

  const calculateAge = (birthDate) => {
    if (!birthDate) return 0;
    const birth = new Date(birthDate);
    const today = new Date();
    let age = today.getFullYear() - birth.getFullYear();
    const monthDiff = today.getMonth() - birth.getMonth();
    if (
      monthDiff < 0 ||
      (monthDiff === 0 && today.getDate() < birth.getDate())
    ) {
      age--;
    }
    return age;
  };

  const handleEdit = () => setIsEditing(true);

  const handleSave = async () => {
    try {
      await widowService.updateWidow(widowId, formData);
      setIsEditing(false);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCancel = () => {
    setIsEditing(false);
    setFormData(widow);
  };

  const handleChange = (e) => {
    const { name, value, type } = e.target;

    const newValue = type === "date" ? value : value;

    const nameParts = name.split(".");
    setFormData((prevData) => {
      const updatedData = { ...prevData };
      if (nameParts.length > 1) {
        updatedData[nameParts[0]] = {
          ...prevData[nameParts[0]],
          [nameParts[1]]: newValue,
        };
      } else {
        updatedData[name] = newValue;
      }
      return updatedData;
    });
  };

  const handleChildChange = (index, e) => {
    const { name, value } = e.target;
    const updatedChildren = formData.orphans.map((child, i) =>
      i === index ? { ...child, [name]: value } : child
    );
    setFormData({ ...formData, orphans: updatedChildren });
  };

  const handleAddChild = () => {
    const newChild = {
      first_name: "",
      last_name: "",
      identity_number: "",
      birth_date: "",
    };
    setFormData((prev) => ({
      ...prev,
      orphans: [...prev.orphans, newChild],
    }));
  };

  const handleRemoveChild = (index) => {
    const updatedChildren = formData.orphans.filter((_, i) => i !== index);
    setFormData({ ...formData, orphans: updatedChildren });
  };

  const handleRelativeChange = (index, e) => {
    const { name, value } = e.target;
    const updatedRelatives = formData.relatives.map((relative, i) =>
      i === index ? { ...relative, [name]: value } : relative
    );
    setFormData({ ...formData, relatives: updatedRelatives });
  };

  const handleAddRelative = () => {
    const newRelative = {
      fl_name: "",
      phone: "",
      email: "",
      relationship_type: "",
    };
    setFormData((prev) => ({
      ...prev,
      relatives: [...prev.relatives, newRelative],
    }));
  };

  const handleRemoveRelative = (index) => {
    const updatedRelatives = formData.relatives.filter((_, i) => i !== index);
    setFormData({ ...formData, relatives: updatedRelatives });
  };

  const renderFields = (fields, handleChange) => (
    <Grid2 container spacing={2}>
      {fields.map((field, index) => (
        <Grid2 xs={12} sm={6} md={4} key={index}>
          <TextField
            id={field.id}
            name={field.name}
            label={field.label}
            value={field.value}
            type={field.type}
            margin="normal"
            InputProps={{
              readOnly: !isEditing,
              disabled: field.disabled,
              required: true,
            }}
            onChange={handleChange}
            fullWidth
          />
        </Grid2>
      ))}
    </Grid2>
  );

  const personalFields = [
    {
      id: "identity-number",
      name: "identity_number",
      label: "מ.ז.",
      value: formData.identity_number || "",
      type: "text",
    },
    {
      id: "first-name",
      name: "first_name",
      label: "שם פרטי",
      value: formData.first_name || "",
      type: "text",
    },
    {
      id: "last-name",
      name: "last_name",
      label: "שם משפחה",
      value: formData.last_name || "",
      type: "text",
    },
    {
      id: "email",
      name: "email",
      label: "אימייל",
      value: formData.email || "",
      type: "text",
    },
    {
      id: "home-phone",
      name: "home_phone",
      label: "טלפון ביתי",
      value: formData.home_phone || "",
      type: "text",
    },
    {
      id: "mobile-phone",
      name: "mobile_phone",
      label: "טלפון נייד",
      value: formData.mobile_phone || "",
      type: "text",
    },
    {
      id: "age",
      name: "age",
      label: "גיל",
      value: formData.age || "",
      type: "number",
      readOnly: true,
      disabled: true,
    },
    {
      id: "birth-date",
      name: "birth_date",
      label: "תאריך לידה",
      value: formData.birth_date || "",
      type: "date",
    },
    {
      id: "hebrew-birth-date",
      name: "hebrew_birth_date",
      label: "יומולדת",
      value: formData.hebrew_birth_date || "",
      type: "text",
    },
    {
      id: "num-of-minor-children",
      name: "num_of_minor_children",
      label: "מספר ילדים בבית",
      value: formData.num_of_minor_children || "",
      type: "number",
    },
    {
      id: "num-of-unmarried-children",
      name: "num_of_unmarried_children",
      label: "מספר ילדים לא נשואים",
      value: formData.num_of_unmarried_children || "",
      type: "number",
    },
    {
      id: "widowhood-date",
      name: "widowhood_date",
      label: "יארצייט",
      value: formData.widowhood_date || "",
      type: "date",
    },
  ];

  const addressFields = [
    {
      id: "address-city",
      name: "address.city",
      label: "עיר",
      value: formData.address?.city || "",
      type: "text",
    },
    {
      id: "address-street",
      name: "address.street",
      label: "רחוב",
      value: formData.address?.street || "",
      type: "text",
    },
    {
      id: "address-num",
      name: "address.num_building",
      label: "מספר בניין",
      value: formData.address?.num_building || "",
      type: "text",
    },
  ];

  const bankFields = [
    {
      id: "bank-account-holder",
      name: "bank_account.holder_name",
      label: "שם בעל החשבון",
      value: formData.bank_account?.holder_name || "",
      type: "text",
    },
    {
      id: "bank-account-number",
      name: "bank_account.account_number",
      label: "מספר חשבון",
      value: formData.bank_account?.account_number || "",
      type: "text",
    },
    {
      id: "bank-branch",
      name: "bank_account.branch",
      label: "סניף בנק",
      value: formData.bank_account?.branch || "",
      type: "text",
    },
    {
      id: "bank-number",
      name: "bank_account.bank_number",
      label: "מספר בנק",
      value: formData.bank_account?.bank_number || "",
      type: "text",
    },
  ];

  const renderChildrenFields = () =>
    (formData.orphans || []).map((child, index) => (
      <Paper key={index} sx={{ marginBottom: 2 }}>
        <Grid2 container spacing={2}>
          {renderFields(
            [
              {
                id: `child-first-name-${index}`,
                name: "first_name",
                label: "שם פרטי",
                value: child.first_name,
                type: "text",
              },
              {
                id: `child-last-name-${index}`,
                name: "last_name",
                label: "שם משפחה",
                value: child.last_name,
                type: "text",
              },
              {
                id: `child-identity-number-${index}`,
                name: "identity_number",
                label: "מ.ז.",
                value: child.identity_number,
                type: "text",
              },
              {
                id: `child-birth-date-${index}`,
                name: "birth_date",
                label: "תאריך לידה",
                value: child.birth_date,
                type: "date",
              },
            ],
            (e) => handleChildChange(index, e)
          )}
        </Grid2>
        {isEditing && (
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => handleRemoveChild(index)}
          >
            הסר ילד
          </Button>
        )}
      </Paper>
    ));

  const renderRelativeFields = () =>
    (formData.relatives || []).map((relative, index) => (
      <Paper key={index} sx={{ marginBottom: 2 }}>
        {renderFields(
          [
            {
              id: `relative-fl-name-${index}`,
              name: "fl_name",
              label: "שם קרוב משפחה",
              value: relative.fl_name,
              type: "text",
            },
            {
              id: `relative-phone-${index}`,
              name: "phone",
              label: "טלפון",
              value: relative.phone,
              type: "text",
            },
            {
              id: `relative-email-${index}`,
              name: "email",
              label: "אימייל",
              value: relative.email,
              type: "text",
            },
            {
              id: `relative-relationship-type-${index}`,
              name: "relationship_type",
              label: "סוג קשר",
              value: relative.relationship_type,
              type: "text",
            },
          ],
          (e) => handleRelativeChange(index, e)
        )}
        {isEditing && (
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => handleRemoveRelative(index)}
          >
            הסר קרוב משפחה
          </Button>
        )}
      </Paper>
    ));

  return (
    <div dir="rtl">
      <h2>פרטי אמא</h2>
      <Paper sx={{ padding: 2, width: "70%", margin: "auto" }}>
        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>פרטים אישיים</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {renderFields(personalFields, handleChange)}
          </AccordionDetails>
        </Accordion>

        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>כתובת</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {renderFields(addressFields, handleChange)}
          </AccordionDetails>
        </Accordion>

        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>פרטי ילדים</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {renderChildrenFields()}
            {isEditing && (
              <Button variant="contained" onClick={handleAddChild}>
                הוסף ילד
              </Button>
            )}
          </AccordionDetails>
        </Accordion>

        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>פרטי בנק</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {renderFields(bankFields, handleChange)}
          </AccordionDetails>
        </Accordion>

        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>קרובי משפחה</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {renderRelativeFields()}
            {isEditing && (
              <Button variant="contained" onClick={handleAddRelative}>
                הוסף קרוב משפחה
              </Button>
            )}
          </AccordionDetails>
        </Accordion>

        <Box sx={{ marginTop: 2 }}>
          {isEditing ? (
            <>
              <Button variant="contained" color="primary" onClick={handleSave}>
                שמור
              </Button>
              <Button
                variant="outlined"
                color="secondary"
                onClick={handleCancel}
                sx={{ marginLeft: 2 }}
              >
                ביטול
              </Button>
            </>
          ) : (
            <Button variant="contained" onClick={handleEdit}>
              עריכה
            </Button>
          )}
        </Box>
      </Paper>
    </div>
  );
};

export default WidowDetails;
