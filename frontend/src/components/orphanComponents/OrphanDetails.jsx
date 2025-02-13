import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import OrphanService from "../../services/OrphanService";
import calculateAge from "../../Utils/Utils";
import BorderColorIcon from "@mui/icons-material/BorderColor";
import {
  Button,
  TextField,
  Grid,
  Paper,
  Typography,
  Card,
  CardContent,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  Grid2,
} from "@mui/material";

const OrphanDetails = ({ orphanId }) => {
  const [orphan, setOrphan] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({ age: 0 });
  const orphanService = new OrphanService();

  useEffect(() => {
    const loadOrphan = async () => {
      try {
        const data = await orphanService.getOrphanById(orphanId);
        // Calculate age
        const age = calculateAge(data[0].birth_date);
        data[0].age = age;
        setFormData(data[0]);
        setOrphan(data[0]);
      } catch (err) {
        console.error(err.message);
      }
    };
    loadOrphan();
  }, [orphanId]);

  useEffect(() => {
    if (formData.birth_date) {
      const age = calculateAge(formData.birth_date);
      setFormData((prev) => ({ ...prev, age }));
    }
  }, [formData.birth_date]);

  const handleEdit = () => {
    setIsEditing(true);
  };
  const handleCancel = () => {
    setFormData(orphan);
    setIsEditing(false);
  };

  const handleSave = async () => {
    try {
      await orphanService.updateOrphan(orphanId, formData);
      setIsEditing(false);
      // אפשר להוסיף כאן הודעת הצלחה
    } catch (err) {
      console.error(err.message);
    }
  };

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
      id: "birth-date",
      name: "birth_date",
      label: "תאריך לידה",
      value: formData.birth_date || "",
      type: "date",
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
  ];

  const schoolFields = [
    {
      id: "school-name",
      name: "school.school_name",
      label: "שם מוסד",
      value: formData.school?.school_name || "",
      type: "text",
    },
    {
      id: "class-name",
      name: "school.class_name",
      label: "כיתה",
      value: formData.school?.class_name || "",
      type: "text",
    },
    {
      id: "teacher-name",
      name: "school.teacher_name",
      label: "שם מורה",
      value: formData.school?.teacher_name || "",
      type: "text",
    },
    {
      id: "teacher-phone",
      name: "school.teacher_phone",
      label: "טל' מורה",
      value: formData.school?.teacher_phone || "",
      type: "text",
    },
  ];

  const renderFields = (fields) => (
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
            onChange={(e) =>
              setFormData({ ...formData, [field.name]: e.target.value })
            }
            fullWidth
          />
        </Grid2>
      ))}
    </Grid2>
  );

  return (
    <Paper style={{ padding: 20 }}>
      <Typography variant="h4">פרטי ילד:</Typography>
      <Button onClick={handleEdit}>
        <BorderColorIcon color="success" />
      </Button>
      <form noValidate autoComplete="off" style={{ marginTop: 20 }}>
        <Grid2 container spacing={2}>
          {renderFields(personalFields)}
          <Grid2 item xs={12} sm={6}>
            <FormControl fullWidth disabled={!isEditing}>
              <InputLabel id="age-group-label">קבוצת גיל</InputLabel>
              <Select
                labelId="age-group-label"
                value={formData.age_group || ""}
                onChange={(e) =>
                  setFormData({ ...formData, age_group: e.target.value })
                }
              >
                <MenuItem value="גן">גן</MenuItem>
                <MenuItem value="חיידר">חיידר</MenuItem>
                <MenuItem value="בית ספר יסודי">בית ספר יסודי</MenuItem>
                <MenuItem value="סמינר">סמינר</MenuItem>
                <MenuItem value="ישיבה קטנה">ישיבה קטנה</MenuItem>
                <MenuItem value="ישיבה גדולה">ישיבה גדולה</MenuItem>
              </Select>
            </FormControl>
          </Grid2>
          <Grid2 item xs={12} sm={6}>
            <FormControl fullWidth disabled={!isEditing}>
              <InputLabel id="gender">מין</InputLabel>
              <Select
                labelId="gender"
                value={formData.gender || ""}
                onChange={(e) =>
                  setFormData({ ...formData, gender: e.target.value })
                }
              >
                <MenuItem value="בן">בן</MenuItem>
                <MenuItem value="בת">בת</MenuItem>
              </Select>
            </FormControl>
          </Grid2>
        </Grid2>
      </form>

      <Card style={{ marginTop: 20 }}>
        <CardContent>
          <Typography variant="h6">פרטי מוסד לימודים:</Typography>
          {renderFields(schoolFields)}
        </CardContent>
      </Card>

      {isEditing && (
        <>
          <Button
            variant="contained"
            color="success"
            onClick={handleSave}
            style={{ marginTop: 20 }}
          >
            שמור
          </Button>
          <Button
            variant="contained"
            color="success"
            onClick={handleCancel}
            style={{ marginTop: 20 }}
          >
            ביטול
          </Button>
        </>
      )}
    </Paper>
  );
};

export default OrphanDetails;
