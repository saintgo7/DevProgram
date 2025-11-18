class AnswerController < ApplicationController
  before_action :set_answer, only: [:show, :edit, :update, :destroy]

  # GET /answer
  def index
    @answers = Answer.all
    render json: @answers
  end

  # GET /answer/1
  def show
    render json: @answer
  end

  # POST /answer
  def create
    @answer = Answer.new(answer_params)

    if @answer.save
      render json: @answer, status: :created
    else
      render json: @answer.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /answer/1
  def update
    if @answer.update(answer_params)
      render json: @answer
    else
      render json: @answer.errors, status: :unprocessable_entity
    end
  end

  # DELETE /answer/1
  def destroy
    @answer.destroy
    head :no_content
  end

  private

  def set_answer
    @answer = Answer.find(params[:id])
  end

  def answer_params
    params.require(:answer).permit(:name)
  end
end
