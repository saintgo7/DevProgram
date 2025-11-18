class StatementController < ApplicationController
  before_action :set_statement, only: [:show, :edit, :update, :destroy]

  # GET /statement
  def index
    @statements = Statement.all
    render json: @statements
  end

  # GET /statement/1
  def show
    render json: @statement
  end

  # POST /statement
  def create
    @statement = Statement.new(statement_params)

    if @statement.save
      render json: @statement, status: :created
    else
      render json: @statement.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /statement/1
  def update
    if @statement.update(statement_params)
      render json: @statement
    else
      render json: @statement.errors, status: :unprocessable_entity
    end
  end

  # DELETE /statement/1
  def destroy
    @statement.destroy
    head :no_content
  end

  private

  def set_statement
    @statement = Statement.find(params[:id])
  end

  def statement_params
    params.require(:statement).permit(:name)
  end
end
