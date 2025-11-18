class ReportController < ApplicationController
  before_action :set_report, only: [:show, :edit, :update, :destroy]

  # GET /report
  def index
    @reports = Report.all
    render json: @reports
  end

  # GET /report/1
  def show
    render json: @report
  end

  # POST /report
  def create
    @report = Report.new(report_params)

    if @report.save
      render json: @report, status: :created
    else
      render json: @report.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /report/1
  def update
    if @report.update(report_params)
      render json: @report
    else
      render json: @report.errors, status: :unprocessable_entity
    end
  end

  # DELETE /report/1
  def destroy
    @report.destroy
    head :no_content
  end

  private

  def set_report
    @report = Report.find(params[:id])
  end

  def report_params
    params.require(:report).permit(:name)
  end
end
