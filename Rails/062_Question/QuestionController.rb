class QuestionController < ApplicationController
  before_action :set_question, only: [:show, :edit, :update, :destroy]

  # GET /question
  def index
    @questions = Question.all
    render json: @questions
  end

  # GET /question/1
  def show
    render json: @question
  end

  # POST /question
  def create
    @question = Question.new(question_params)

    if @question.save
      render json: @question, status: :created
    else
      render json: @question.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /question/1
  def update
    if @question.update(question_params)
      render json: @question
    else
      render json: @question.errors, status: :unprocessable_entity
    end
  end

  # DELETE /question/1
  def destroy
    @question.destroy
    head :no_content
  end

  private

  def set_question
    @question = Question.find(params[:id])
  end

  def question_params
    params.require(:question).permit(:name)
  end
end
