class IssueController < ApplicationController
  before_action :set_issue, only: [:show, :edit, :update, :destroy]

  # GET /issue
  def index
    @issues = Issue.all
    render json: @issues
  end

  # GET /issue/1
  def show
    render json: @issue
  end

  # POST /issue
  def create
    @issue = Issue.new(issue_params)

    if @issue.save
      render json: @issue, status: :created
    else
      render json: @issue.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /issue/1
  def update
    if @issue.update(issue_params)
      render json: @issue
    else
      render json: @issue.errors, status: :unprocessable_entity
    end
  end

  # DELETE /issue/1
  def destroy
    @issue.destroy
    head :no_content
  end

  private

  def set_issue
    @issue = Issue.find(params[:id])
  end

  def issue_params
    params.require(:issue).permit(:name)
  end
end
