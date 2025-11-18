class DashboardController < ApplicationController
  before_action :set_dashboard, only: [:show, :edit, :update, :destroy]

  # GET /dashboard
  def index
    @dashboards = Dashboard.all
    render json: @dashboards
  end

  # GET /dashboard/1
  def show
    render json: @dashboard
  end

  # POST /dashboard
  def create
    @dashboard = Dashboard.new(dashboard_params)

    if @dashboard.save
      render json: @dashboard, status: :created
    else
      render json: @dashboard.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /dashboard/1
  def update
    if @dashboard.update(dashboard_params)
      render json: @dashboard
    else
      render json: @dashboard.errors, status: :unprocessable_entity
    end
  end

  # DELETE /dashboard/1
  def destroy
    @dashboard.destroy
    head :no_content
  end

  private

  def set_dashboard
    @dashboard = Dashboard.find(params[:id])
  end

  def dashboard_params
    params.require(:dashboard).permit(:name)
  end
end
