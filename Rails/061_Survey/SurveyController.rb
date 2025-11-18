class SurveyController < ApplicationController
  before_action :set_survey, only: [:show, :edit, :update, :destroy]

  # GET /survey
  def index
    @surveys = Survey.all
    render json: @surveys
  end

  # GET /survey/1
  def show
    render json: @survey
  end

  # POST /survey
  def create
    @survey = Survey.new(survey_params)

    if @survey.save
      render json: @survey, status: :created
    else
      render json: @survey.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /survey/1
  def update
    if @survey.update(survey_params)
      render json: @survey
    else
      render json: @survey.errors, status: :unprocessable_entity
    end
  end

  # DELETE /survey/1
  def destroy
    @survey.destroy
    head :no_content
  end

  private

  def set_survey
    @survey = Survey.find(params[:id])
  end

  def survey_params
    params.require(:survey).permit(:name)
  end
end
