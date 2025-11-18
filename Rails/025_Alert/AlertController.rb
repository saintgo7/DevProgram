class AlertController < ApplicationController
  before_action :set_alert, only: [:show, :edit, :update, :destroy]

  # GET /alert
  def index
    @alerts = Alert.all
    render json: @alerts
  end

  # GET /alert/1
  def show
    render json: @alert
  end

  # POST /alert
  def create
    @alert = Alert.new(alert_params)

    if @alert.save
      render json: @alert, status: :created
    else
      render json: @alert.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /alert/1
  def update
    if @alert.update(alert_params)
      render json: @alert
    else
      render json: @alert.errors, status: :unprocessable_entity
    end
  end

  # DELETE /alert/1
  def destroy
    @alert.destroy
    head :no_content
  end

  private

  def set_alert
    @alert = Alert.find(params[:id])
  end

  def alert_params
    params.require(:alert).permit(:name)
  end
end
