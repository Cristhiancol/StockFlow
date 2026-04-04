import React from 'react';
import { Line } from 'react-chartjs-2';
import { Card, Button, Grid } from 'react-bootstrap';

// Sample data for stock levels and KPIs
const stockLevelsData = {
    labels: ['January', 'February', 'March', 'April', 'May'],
    datasets: [{
        label: 'Stock Levels',
        data: [3, 2, 5, 4, 6],
        fill: false,
        borderColor: '#10b981',
    }]
};

const KPIData = [
    { label: 'Total Sales', value: '$20,000', color: '#0ea5e9' },
    { label: 'Stock Turnover', value: '75%', color: '#f97316' },
    { label: 'Low Stock Alerts', value: '2', color: '#ef4444' },
];

const Dashboard = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h2>Inventory Dashboard</h2>
            <Grid>
                <Grid.Row>
                    <Grid.Column width={8}>
                        <Card>
                            <Card.Header>Stock Levels</Card.Header>
                            <Card.Body>
                                <Line data={stockLevelsData} />
                            </Card.Body>
                        </Card>
                    </Grid.Column>
                    <Grid.Column width={8}>
                        <Card>
                            <Card.Header>KPI Metrics</Card.Header>
                            <Card.Body>
                                {KPIData.map((kpi, index) => (
                                    <div key={index} style={{ color: kpi.color }}>
                                        <strong>{kpi.label}:</strong> {kpi.value}
                                    </div>
                                ))}
                            </Card.Body>
                        </Card>
                    </Grid.Column>
                </Grid.Row>
                <Grid.Row>
                    <Grid.Column width={12}>
                        <Card>
                            <Card.Header>Alerts Panel</Card.Header>
                            <Card.Body>
                                <Button variant="danger">View Low Stock Alerts</Button>
                            </Card.Body>
                        </Card>
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </div>
    );
};

export default Dashboard;